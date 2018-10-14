import requests
import json
import csv
import fake_useragent

class Maoyan():
	headers = {
	        "User-Agent": fake_useragent.UserAgent(verify_ssl=False).random,
	        "Host":"m.maoyan.com",
	        "Referer":"http://m.maoyan.com/movie/1217236/comments?_v_=yes"
	    }

	def __init__(self,url):
		self.url = url

	def get_json(self):
		response = requests.get(self.url,headers = self.headers)
		comments_json = json.loads(response.text)  # 字符串转json对象
		print(comments_json)
		return comments_json

	def get_data(self,json_comment):
		comments = json_comment['cmts']
		print(len(comments))
		list_info = []
		for data in comments:
			cityName = data['cityName']
			content = data['content']
			nickName = data['nickName']
			userLevel = data['userLevel']
			score = data['score'] 
			time = data['time']  #2018-10-13 09:17:07
			# 有的人没有设置性别 初步判断 1男生， 2女生，0未知
			if "gender" in data:    
				gender = data["gender"]
			else:
				gender = 0

			list_one = [time[0:10],cityName,nickName,gender,userLevel,score,content]
			list_info.append(list_one)
		self.save_data(list_info)

	def save_data(self,comment_list):
		with open('maoyan.csv','w',encoding = 'utf-8-sig') as f:
			f_csv = csv.writer(f)
			f_csv.writerow(['时间','城市','昵称','性别','等级','评分','评论'])
			f_csv.writerows(comment_list)

def spider_maoyan():
	offset = 15
	start_time = '2018-09-21'
	comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset,start_time)
	maoyan = Maoyan(comment_api)
	json_comment = maoyan.get_json()
	maoyan.get_data(json_comment)

if __name__ == '__main__':
	spider_maoyan()
