import csv
import re
import jieba

gender = []
time = []
level = []
score = []

def read_csv():
	comment_content = ''
	with open('maoyan.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			if reader.line_num > 1:
				gender.append(row[3])
				time.append(row[0])
				level.append(row[4])
				score.append(row[5])
				comment_content = comment_content + row[6]

		print(comment_content)
		return comment_content




# 评论者性别分布可视化
def sex_render(gender):
	from pyecharts import Pie
	attr = ['男','女','未知']  #1男生， 2女生，0未知
	value = []
	value.append(gender.count('1'))
	value.append(gender.count('2'))
	value.append(gender.count('0'))
	Pie("性别比例").add("",attr,value,is_label_show = True).render('sex.html')

# 每日评论数曲线
def comment_num_render(time):
	from pyecharts import Line
	attr = list(set(time))
	attr.sort(key=time.index)
			
	v1 = []
	for x in attr:
		v1.append(time.count(x))
	Line("每日评论数").add("",attr,v1,is_label_show = True,is_smooth = True).render("comment_num.html")

def level_render(level):
	from pyecharts import Pie
	attr = list(set(level))
	value = []
	for x in attr:
		value.append(level.count(x))
	Pie("评论者等级分布",title_pos='center').add(
		"等级",
		attr,value,
		is_label_show = True,
		radius = [40 , 75],
		legend_orient="vertical",
		legend_pos="left"
		).render("level.html")

def score_rose_render(score):
	from pyecharts import Pie
	attr = list(set(score))
	value = []
	for x in attr:
		value.append(score.count(x))
	Pie("评分玫瑰饼图分布",title_pos='center').add(
		"",
		attr,
		value,
		is_label_show=True,
		is_legend_show=False,
		radius = [40 , 75],
		# rosetype="radius",
		rosetype="area"
		).render("score_rose.html")

#定义个函数式用于分词
def jiebaclearText(text):

	#定义一个空的列表，将去除的停用词的分词保存
	mywordList=[]
	text = re.sub('[,，。. \r\n]', '', text)
	#进行分词
	seg_list=jieba.cut(text,cut_all=False)
	#将一个generator的内容用/连接
	listStr='/'.join(seg_list)
	listStr = listStr.replace("class","")
	listStr = listStr.replace("span", "")
	listStr = listStr.replace("悲伤逆流成河", "")
	#打开停用词表
	f_stop=open('stopwords.txt',encoding="utf8")
	#读取
	try:
		f_stop_text=f_stop.read()
	finally:
		f_stop.close()#关闭资源
	#将停用词格式化，用\n分开，返回一个列表
	f_stop_seg_list=f_stop_text.split("\n")
	#对默认模式分词的进行遍历，去除停用词
	for myword in listStr.split('/'):
		#去除停用词
		if not(myword.split()) in f_stop_seg_list and len(myword.strip())>1:
			mywordList.append(myword)
	return ' '.join(mywordList)

content = read_csv()

cont = jiebaclearText(content)
print(cont)

sex_render(gender)
comment_num_render(time)
level_render(level)
score_rose_render(score)
