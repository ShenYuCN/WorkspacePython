import csv

def read_csv():
	with open('maoyan.csv') as file:
		


# 评论者性别分布可视化
# def sex_distribution(gender):
# 	# print(gender)
# 	from pyecharts import Pie
# 	list_num = []
# 	list_num.append(gender.count('0')) # 未知
# 	list_num.append(gender.count('1')) # 男
# 	list_num.append(gender.count('2')) # 女
# 	attr = ["其他","男","女"]
# 	pie = Pie("性别饼图")
# 	pie.add("", attr, list_num, is_label_show=True)
# 	pie.render("H:\PyCoding\spider_maoyan\picture\sex_pie.html")
