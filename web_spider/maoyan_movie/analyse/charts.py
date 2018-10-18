import csv

gender = []
time = []
def read_csv():
	with open('maoyan.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			if reader.line_num > 1:
				gender.append(row[3])
				time.append(row[0])




# 评论者性别分布可视化
def sex_render(gender):
	from pyecharts import Pie
	attr = ['男','女','未知']  #1男生， 2女生，0未知
	value = []
	value.append(gender.count('1'))
	value.append(gender.count('2'))
	value.append(gender.count('0'))
	Pie("性别比例").add("",attr,value,is_label_show = True).render('sex.html')

def comment_num_render(time):
	from pyecharts import Line

	print(time)
	print(set(time))

	time_list = list(set(time))
	print(time_list)
	# time_dict = {time_list[i]: 0 for i in range(len(time_list))}
	# time_num = []
	# for i in range(len(time_list)):
	# 	time_dict[time_list[i]] = time.count(time_list[i])
	# # 根据数量(字典的键值)排序
	# sort_dict = sorted(time_dict.items(), key=lambda d: d[0], reverse=False)
	# time_name = []
	# time_num = []
	# print(sort_dict)
	# for i in range(len(sort_dict)):
	# 	time_name.append(sort_dict[i][0])
	# 	time_num.append(sort_dict[i][1])
			


	# attr = []
	# for x in time:
	# 	if x not in attr:
	# 		attr.append(x)
	# for x in attr:
	# 	v1.append(time.count(x))
	# Line("每日评论数").add("",attr,v1,is_label_show = True).render("comment_num.html")



read_csv()
sex_render(gender)
comment_num_render(time)
