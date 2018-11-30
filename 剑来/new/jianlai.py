import requests
import re
import csv
import simplejson



class Jianlai(object):
	"""总管，剑来"""
	def get_save_csv(self):
		respose = requests.get('http://book.zongheng.com/showchapter/672340.html').text
		pattern = re.compile('title="(.*?)">')
		"""
        <li data-rid="6"><a href="//vipreader.qidian.com/chapter/1010496369/392128365" target="_blank" data-eid="qd_G55" data-cid="//vipreader.qidian.com/chapter/1010496369/392128365" title="首发时间：2017-12-03 20:00:00 章节字数：2114">第二十九章且看山道来一鬼</a>              
            <em class="iconfont ">&#xe63c;</em>
        </li>           
        """
		with open('jianlai.csv','w', encoding = 'utf-8-sig') as f:
			f_csv = csv.writer(f)
			for content in pattern.findall(respose):
				# 第十六章 休想 字数：3672 更新时间：2017-06-17 23:56 
				if content.startswith("第"):
					name_r = content.index('字数') - 1
					num_l = content.index('：') + 1
					num_r = content.index('更新时间') - 1
					time_l = content.index('：',num_r) + 1
					time_r = len(content) - 1

					time = content[time_l:time_r]
					limit = '2018-01-01 00:00'
					if  time > limit:
						print('enter')
						arr = [content[:name_r],content[num_l:num_r],time]
						# print(arr)
						f_csv.writerow(arr)


class Maoni(object):
	"""猫腻，大道朝天"""
	def __init__(self):
		pass
		
	def get_save_csv(self):
		respose = requests.get('https://book.qidian.com/info/1010496369#Catalog').text
		pattern = re.compile('title="(.*?)">(.*?)</a>')
 		# <li data-rid="31"><a href="//read.qidian.com/chapter/_h17RCSkeXScikCo3ZPkrg2/gyIJWIpOlmzwrjbX3WA1AA2" target="_blank" data-eid="qd_G55" data-cid="//read.qidian.com/chapter/_h17RCSkeXScikCo3ZPkrg2/gyIJWIpOlmzwrjbX3WA1AA2" 
 		# title="首发时间：2017-10-29 20:00:00 章节字数：2016">第三十章一朵奇葩入云来</a></li>

		with open('maoni.csv','w', encoding = 'utf-8-sig') as f:
			f_csv = csv.writer(f)
			for content in pattern.findall(respose):
				# ('首发时间：2017-10-15 09:44:53 章节字数：2536', '第一章 三千里禁')
				if content[0].startswith('首发时间') and content[1].startswith('第'):
					print(content)
					time_num_str = content[0]
					time = time_num_str[5:24]
					num_l = time_num_str.index('章节字数：') + 5
					limit = '2018-01-01 00:00'
					if  time > limit:
						arr = [content[1], time_num_str[num_l:len(time_num_str)], time]
						f_csv.writerow(arr)


class Sanshao(object):
	"""三少，斗罗大陆III龙王传说,8月24日之后，大龟甲师，11月22日之后，斗罗大陆外传唐门英雄传"""
	def __init__(self):
		pass
		
	def get_save_csv(self):
		respose = requests.get('https://book.qidian.com/info/3681560#Catalog').text
		pattern = re.compile('title="(.*?)">(.*?)</a>')
		  # <li data-rid="17"><a href="//read.qidian.com/chapter/ndXhlu2kOVl51l-ULjeaVw2/01cS72bfgXpp4rPq4Fd4KQ2" target="_blank" data-eid="qd_G55" data-cid="//read.qidian.com/chapter/ndXhlu2kOVl51l-ULjeaVw2/01cS72bfgXpp4rPq4Fd4KQ2" 
		  # title="首发时间：2018-08-28 07:00:00 章节字数：3205">第十七章 王老虎看病</a>

		with open('sanshao1.csv','w', encoding = 'utf-8-sig') as f:
			f_csv = csv.writer(f)
			for content in pattern.findall(respose):
				print(content)
				# ('首发时间：2017-10-15 09:44:53 章节字数：2536', '第一章 三千里禁')
				if content[0].startswith('首发时间') and content[1].startswith('第'):
					print(content)
					time_num_str = content[0]
					time = time_num_str[5:24]
					num_l = time_num_str.index('章节字数：') + 5
					arr = [content[1], time_num_str[num_l:len(time_num_str)], time]
					f_csv.writerow(arr)

            
class Chendong(object):
	"""辰东，圣墟"""
	def __init__(self):
		pass
		
	def get_save_csv(self):
		str_content = open('chendong.json').read()
		dict_content = simplejson.loads(str_content)
		vs = dict_content['data']['vs']
		with open('chendong.csv','w', encoding = 'utf-8-sig') as f:
			f_csv = csv.writer(f)
			for x in vs:
				cs = x['cs']
				for model in cs:
					if model['cnt'] > 1000 and model['uT'] > '2018-01-01 00:00':
						f_csv.writerow([model['cN'],model['cnt'],model['uT']])



	
if __name__ == '__main__':
	# jianlai = Jianlai()
	# jianlai.get_save_csv()

	# maoni = Maoni()
	# maoni.get_save_csv()

	# sanshao = Sanshao()
	# sanshao.get_save_csv()



	chendong = Chendong()
	chendong.get_save_csv()
