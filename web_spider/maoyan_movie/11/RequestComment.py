import requests
# import fake_useragent
from fake_useragent import UserAgent

# 经验证 猫眼不写header都可以正常请求
headers = {
		"User-Agent": UserAgent(verify_ssl=False).random,
		"Host": "m.maoyan.com",
		"Referer": "http://m.maoyan.com/movie/1217236/comments?_v_=yes"
}
offset = 0
# 电影是 2018.9.21 上映，经验证，这个时间填今天也行，应该无关紧要
startTime = '2018-09-21'
url = 'http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset,startTime)
response = requests.get(url,headers = headers)
print(response.text)

"""

import json
headers = {
        "User-Agent": UserAgent(verify_ssl=False).random,
        "Host":"m.maoyan.com",
        "Referer":"http://m.maoyan.com/movie/1217236/comments?_v_=yes"
    }
# 猫眼电影短评接口
offset = 0
# 电影是2018.9.21上映的
startTime = '2018-09-21'
comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1217236.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset,startTime)
# 发送get请求
response_comment = requests.get(comment_api,headers = headers)
json_comment = response_comment.text
json_comment = json.loads(json_comment)
print(json_comment)
"""