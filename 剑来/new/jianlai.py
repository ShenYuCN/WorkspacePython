import requests
import re
import csv
import simplejson




class ZongHengSpider(object):
	"""起点爬目录，格式一致, 以 剑来，总管 为例"""
	def __init__(self,url,savename):
		self.url = url
		self.savename = savename

	def get_save_csv(self):
		respose = requests.get(self.url).text
		pattern = re.compile('title="(.*?)">')
		"""
		<li data-rid="6"><a href="//vipreader.qidian.com/chapter/1010496369/392128365" target="_blank" data-eid="qd_G55" data-cid="//vipreader.qidian.com/chapter/1010496369/392128365" title="首发时间：2017-12-03 20:00:00 章节字数：2114">第二十九章且看山道来一鬼</a>              
			<em class="iconfont ">&#xe63c;</em>
		</li>           
		"""
		with open(self.savename,'w', encoding = 'utf-8-sig') as f:
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
						arr = [content[:name_r],content[num_l:num_r],time]
						f_csv.writerow(arr)


class QidianSpider(object):
	"""起点爬目录，格式一致，以 猫腻，大道朝天  为例"""
	def __init__(self,url,savename):
		self.url = url
		self.savename = savename
		
	def get_save_csv(self):
		respose = requests.get(self.url).text
		pattern = re.compile('title="(.*?)">(.*?)</a>')
		# <li data-rid="31"><a href="//read.qidian.com/chapter/_h17RCSkeXScikCo3ZPkrg2/gyIJWIpOlmzwrjbX3WA1AA2" target="_blank" data-eid="qd_G55" data-cid="//read.qidian.com/chapter/_h17RCSkeXScikCo3ZPkrg2/gyIJWIpOlmzwrjbX3WA1AA2" 
		# title="首发时间：2017-10-29 20:00:00 章节字数：2016">第三十章一朵奇葩入云来</a></li>

		with open(self.savename,'w', encoding = 'utf-8-sig') as f:
			f_csv = csv.writer(f)
			for content in pattern.findall(respose):
				# ('首发时间：2017-10-15 09:44:53 章节字数：2536', '第一章 三千里禁')
				if content[0].startswith('首发时间') and content[1].startswith('第'):
					print(content)
					time_num_str = content[0]
					time = time_num_str[5:24]
					num_l = time_num_str.index('章节字数：') + 5
					limit_l = '2018-01-01 00:00'
					limit_r = '2018-12-01 00:00'

					if  time > limit_l and time < limit_r:
						arr = [content[1], time_num_str[num_l:len(time_num_str)], time]
						f_csv.writerow(arr)


			
class QidianParseJsonFile(object):
	"""起点抓取的json，解析存储，以 辰东，圣墟 为例"""
	def __init__(self,jsonname,savename):
		self.jsonname = jsonname
		self.savename = savename
		
	def get_save_csv(self):
		str_content = open(self.jsonname).read()
		dict_content = simplejson.loads(str_content)
		vs = dict_content['data']['vs']

		with open(self.savename,'w', encoding = 'utf-8-sig') as f:
			f_csv = csv.writer(f)
			for x in vs:
				cs = x['cs']
				for model in cs:
					if  model['cN'].startswith('第') and model['cnt'] > 1000 and model['uT'] > '2018-01-01 00:00' and model['uT'] < '2018-12-01 00:00':
						f_csv.writerow([model['cN'],model['cnt'],model['uT']])



	
if __name__ == '__main__':
	# 总管，剑来
	# jianlai = ZongHengSpider('http://book.zongheng.com/showchapter/672340.html','jianlai.csv')
	# jianlai.get_save_csv()


	# 猫腻，大道朝天
	# maoni = QidianSpider('https://book.qidian.com/info/1010496369#Catalog','maoni.csv')
	# maoni.get_save_csv()

	# 辰东，圣墟
	# chendong = QidianParseJsonFile('chendong.json','chendong.csv')
	# chendong.get_save_csv()

	"""
	# 耳根，三寸人间 ergen_sancunrenjian
	ergen = QidianSpider('https://book.qidian.com/info/1010327039#Catalog','ergen_sancunrenjian.csv')
	ergen.get_save_csv()

	# 耳根，一念永恒   ergen_yinianyonghang.json
	ergen_yinianyonghang = QidianParseJsonFile('ergen_yinianyonghang.json','ergen_yinianyonghang.csv')
	ergen_yinianyonghang.get_save_csv()

	with open('ergen.csv','w') as f:
		f_csv_writer = csv.writer(f)
		with open('ergen_yinianyonghang.csv') as ergen_1:
			ergen_1_reader = csv.reader(ergen_1)
			for line in ergen_1_reader:
				f_csv_writer.writerow(line)
		with open('ergen_sancunrenjian.csv') as ergen_1:
			ergen_1_reader = csv.reader(ergen_1)
			for line in ergen_1_reader:
				f_csv_writer.writerow(line)
		
	"""


	# 宅猪 牧神记 
	# zhaizhu = QidianParseJsonFile('zhaizhu.json','zhaizhu.csv')
	# zhaizhu.get_save_csv()


	# 愤怒的香蕉 赘婿 
	zhuixu = QidianParseJsonFile('zhuixu.json','zhuixu.csv')
	zhuixu.get_save_csv()

	# 我吃西红柿 飞剑问道
	# fanqie = QidianSpider('https://book.qidian.com/info/1010468795#Catalog','fanqie.csv')
	# fanqie.get_save_csv()


