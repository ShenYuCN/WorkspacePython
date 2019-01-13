import re
import requests
from fake_useragent import UserAgent
import csv

# from fake_useragent import UserAgent
# import json
# headers = {
#         "User-Agent": UserAgent(verify_ssl=False).random,
#         "Host":"m.maoyan.com",
#         "Referer":"http://m.maoyan.com/movie/1217236/comments?_v_=yes"
#     }


def request(index):

	headers = {
	'User-Agent':UserAgent().random
	}

	# headers = {
	# # 'Cookie':'UM_distinctid=168404755a5153-0078a6dbf1e4d8-10346655-fa000-168404755a6358; JSESSIONID=0000_1lbQxjibZrAB3XgNIgmkAg:-1; CNZZDATA1256895572=1899151880-1547266529-%7C1547289170',
	# # 'Referer':'http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlist',
	# # 'Host':'www.chinadrugtrials.org.cn',
	# # 'Connection':'keep-alive',
	# # 'Content-Length':'194',
	# # 'Pragma':'no-cache',
	# # 'Cache-Control':'no-cache',
	# # 'Upgrade-Insecure-Requests':'1',
	# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	# # 'Origin':'http://www.chinadrugtrials.org.cn',
	# # 'Content-Type':'application/x-www-form-urlencoded',
	# # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	# # 'Accept-Encoding':'gzip, deflate',
	# # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8'
	# }


#### 列表页请求
	# data_form = {
	# # 'sort':'asc',
	# 'sort2':'desc',
	# # 'rule':'CTR',
	# # 'currentpage':'373',
	# # 'pagesize':'20',
	# }
	# respose  = requests.post('http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlist', headers=headers,data=data_form)


# ckm_id: 468
# ckm_index: 23
# sort: asc
# sort2: desc
# rule: CTR
# currentpage: 2
# pagesize: 20
# keywords: 
# reg_no: CTR

	data_form = {
	'ckm_index':index,
	# ckm_id: 198
	# 'ckm_id':'198',
	'sort':'asc',
	'sort2':'desc',
	'rule':'CTR',
	'currentpage':'400',
	'pagesize':'20',
	'reg_no':'CTR'
	}
	respose  = requests.post('http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlistdetail', headers=headers,data=data_form)


	# print(respose.url)
	# print(respose.text)
	anylise(respose.text)
	# >>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})

# ckm_id: 
# ckm_index: 
# sort: asc
# sort2: desc
# rule: CTR
# currentpage: 373
# pagesize: 20
# keywords: 
# reg_no: CTR
# indication: 
# case_no: 
# drugs_name: 
# drugs_type: 
# appliers: 
# communities: 
# researchers: 
# agencies: 
# state: 



# import requests
# from fake_useragent import UserAgent
# import json
# headers = {
#         "User-Agent": UserAgent(verify_ssl=False).random,
#         "Host":"m.maoyan.com",
#         "Referer":"http://m.maoyan.com/movie/1217236/comments?_v_=yes"
#     }
# # 猫眼电影短评接口
# offset = 0
# # 电影是2018.9.21上映的 
# startTime = '2018-10-14'  
# comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset,startTime)
# # 发送get请求
# response_comment = requests.get(comment_api,headers = headers)
# json_comment = response_comment.text
# print(json_comment)
# json_comment = json.loads(json_comment)
# # print(json_comment)


def anylise(file):
	# file = open('dmo1.html').read()
	# file = open('demo.html').read()
	# print(file)

	# pattern = re.compile('data-original="(.*?)\salt="(.*?)"')


	# result = pattern.search(file)
	# print(result.group())

	# print('0   ' + result.group(0))
	# print('1   '+result.group(1))
	# print('2   '+result.group(2))



	mlist = []
	pattern_date = re.compile('首次公示信息日期：.*?<td>(.*?)</td>',re.DOTALL)
	date = pattern_date.search(file)
	mlist.append(date.group(1).strip())


	# pattern = re.compile('首次公示信息日期：.*?<td>.*?(.*?).*?</td>.*?登记号：.*?FFFFFF">(.*?)</td>.*?适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)
	# pattern = re.compile('登记号：.*?FFFFFF">(.*?)</td>.*?适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)



	pattern_code = re.compile('登记号：.*?FFFFFF">(.*?)</td>',re.DOTALL)
	code = pattern_code.search(file)
	mlist.append(code.group(1).strip())


	# pattern = re.compile('登记号：.*?FFFFFF">(.*?)</td>',re.DOTALL)


	pattern_func = re.compile('适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)
	func = pattern_func.search(file)
	mlist.append(func.group(1).strip())




	# pattern = re.compile('适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)
	# result = pattern.search(file)

	# print(result.groups())

	# print('1   '+result.group(1))
	# print(result.group(1).strip())
	# print('2   '+result.group(2))

	# print('3   '+result.group(3))
	# print(mlist)


	pattern_author = re.compile('单位名称.*?#FFFFFF">(.*?)</td>',re.DOTALL)
	result = pattern_author.search(file)


	for info in pattern_author.findall(file):
		mlist.append(info.strip())
		# print(info.strip())


	# print(result.groups())

	# print(result.group(1).strip())

	# mlist.append(author.group(1).strip())

									          	

	pattern_author_sub = re.compile('<td align="center">.*?<td align="left" height="30">(.*?)</.*?<td align="left">',re.DOTALL)
	# author_sub = pattern_author.search(file)

	for info in pattern_author_sub.findall(file):
		mlist.append(info.strip())
		# print(info.strip())

		# mlist.append(info.strip())

	print(mlist[1])
	write_file(mlist)


def write_file(data):
	with open('drugs.csv', 'a', encoding = 'utf-8-sig') as f :
		f_csv = csv.writer(f)
		f_csv.writerow(data)



if __name__ == '__main__':

	# request(62)
	# file = open('dmo1.html').read()
	# anylise(file)

	with open('drugs.csv', 'a', encoding = 'utf-8-sig') as f :
			f_csv = csv.writer(f)
			f_csv.writerow(['首次公示信息日期','登记号','适应症','主要研究者信息'])

	for x in range(1,7444):
		request(x)

	# for x in range(1,2):
	# 	url = 'https://www.doutula.com/photo/list/?page=%d' % x
	# 	get_url(url)

