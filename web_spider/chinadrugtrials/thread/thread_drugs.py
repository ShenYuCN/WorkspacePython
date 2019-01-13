import re
import requests
from fake_useragent import UserAgent
import csv

from threading import Thread
from queue import Queue


mqueue = Queue()
headers = {
	'User-Agent':UserAgent().random
	}


def anylise(file):

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


def produce_req_body():

	
	for x in range(20*51+15,7444):
		data_form = {
		'ckm_index':x,
		# 'ckm_id':'198',
		'sort':'asc',
		'sort2':'desc',
		'rule':'CTR',
		'currentpage':'400',
		'pagesize':'20',
		'reg_no':'CTR'
		}
		mqueue.put(data_form) # 生成请求体存入队列，等待其他线程提取



def get_info():
		while not mqueue.empty(): # 保证请求体遍历结束后能退出线程
			data_form = mqueue.get() # 从队列中获取请求体

			print(data_form)
			respose  = requests.post('http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlistdetail', headers=headers,data=data_form)
			anylise(respose.text)
		  




def run():
	produce_req_body()

	ths = []
	for _ in range(10):
		th = Thread(target=get_info)
		th.start()
		ths.append(th)
	for th in ths:
		th.join()


if __name__ == '__main__':

	with open('drugs.csv', 'a', encoding = 'utf-8-sig') as f :
			f_csv = csv.writer(f)
			f_csv.writerow(['首次公示信息日期','登记号','适应症','主要研究者信息'])

	run()

