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

		return comment_content


stopwords_path = 'maoyan_stopwords.txt'
# 评论词云分析
def word_cloud(content):
	from pyecharts import WordCloud
	content_list = content.split(' ')
	seg_list = list(set(content_list))

	myDict = {}

	for word in seg_list:
		myDict[word] = content_list.count(word)

	attr = []
	v = []
	for (key,value) in myDict.items():
		if value > 1:
			attr.append(key)
			v.append(value)
	

	wordcloud = WordCloud("影评词云",width=1300, height=620)
	wordcloud.add("sss",attr,v,word_size_range=[20,100],shape='star')
	wordcloud.render("world_cloud.html")
	# shape -> list
	# 词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'可选

	# import jieba, re, numpy
	# from pyecharts import WordCloud
	# import pandas as pd

	# # 去除所有评论里多余的字符
	# content = content.replace(" ", ",")
	# content = content.replace(" ", "、")
	# content = re.sub('[,，。. \r\n]', '', content)
		
	# segment = jieba.lcut(content)
	# words_df = pd.DataFrame({'segment': segment})
	# # quoting=3 表示stopwords.txt里的内容全部不引用
	# stopwords = pd.read_csv(stopwords_path, index_col=False, quoting=3, sep="\t", names=['stopword'],
	# 	                        encoding='utf-8')
	# words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
	# words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
	# words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
	# test = words_stat.head(500).values
	# codes = [test[i][0] for i in range(0, len(test))]
	# counts = [test[i][1] for i in range(0, len(test))]
	# wordcloud = WordCloud(width=1300, height=620)
	# wordcloud.add("影评词云", codes, counts, word_size_range=[20, 100])
	# wordcloud.render("wordcloud.html")

#定义个函数式用于分词
def jiebaclearText(text):
	#定义一个空的列表，将去除的停用词的分词保存
	mywordList=[]
	text = re.sub('[,，。. \r\n]', '', text)

	# 强制调高词频
	# jieba.add_word('台中') 或者 jieba.suggest_freq('台中', True)

	# jieba.add_word('校园暴力')
	# jieba.suggest_freq('校园暴力')
	
	# jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用
	# jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
	seg_list = jieba.cut(text,cut_all=False)


	# 如果自己需要去掉个别停用词可以在这里替换  或者加入 stopwords_path 文件
	# listStr='/'.join(seg_list)
	# listStr = listStr.replace("真的","")
	# listStr = listStr.replace("span", "")
	# listStr = listStr.replace("悲伤逆流成河", "")


	#打开停用词表
	f_stop = open(stopwords_path,encoding="utf8")
	#读取
	try:
		f_stop_text = f_stop.read()
	finally:
		f_stop.close()#关闭资源

	#将停用词格式化，用\n分开，返回一个列表
	f_stop_seg_list = f_stop_text.split("\n")


	#对默认模式分词的进行遍历，去除停用词
	for myword in seg_list:
		#去除停用词
		if not(myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
			mywordList.append(myword)
	return ' '.join(mywordList)


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


content = read_csv()

segment_list = jiebaclearText(content)
print(segment_list)
word_cloud(segment_list)

sex_render(gender)
comment_num_render(time)
level_render(level)
score_rose_render(score)
