import json
import os
import csv
original_str = open('response.json').read()
json_comment = json.loads(original_str)


comments = json_comment['cmts'] # 评论列表
print(len(comments))

# 遍历一组数据（15个），生成一个列表
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

print(list_info)

with open('aaa.csv','w',encoding='utf-8-sig') as f:
	writer = csv.writer(f)
	writer.writerow(['时间','城市','昵称','性别','等级','评分','评论'])
	writer.writerows(list_info)

# file = open('aaa.csv','w')
# for 
# if os.path.exists('aaa.csv'):
# 	print('aaa.cvs 存在')
# 	file_size = os.path.getsize('aaa.csv')
# 	if file_size == 0:


# else:
# 	print('aaa.cvs 不存在，要创建')
# 	file = open('aaa.cvs','w')
# 	print('aaa.cvs 创建成功')

