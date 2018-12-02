from pyecharts import Bar
from pyecharts import configure
import csv




class Analyse(object):
	"""网络小说作者2018年更新分析"""

	# 耳根  香蕉   有几个月没更新，临时手动改数据,数据不干净
	allinfo = [
				('辰东-圣墟','chendong.csv'),
				('总管-剑来','jianlai.csv'),
				('猫腻-大道朝天','maoni.csv'),
				('耳根-三寸/一念','ergen.csv'),
				('宅猪-牧神记','zhaizhu.csv'),
				('香蕉-赘婿 ','zhuixu.csv'),
				('番茄-飞剑问道','fanqie.csv')
				]

				# ('辰东-圣墟','chendong.csv'),
				# ('总管-剑来','jianlai.csv'),
				# ('猫腻-大道朝天','maoni.csv'),
				# ('耳根-三寸人间&一念永恒','ergen.csv'),
				# ('宅猪-牧神记','zhaizhu.csv'),
				# ('愤怒的香蕉-赘婿 ','zhuixu.csv'),
				# ('我吃西红柿-飞剑问道','fanqie.csv')

	title = '贴吧@桑桑好桑心'
	subtitle = '数据整理自起点和纵横，截止2018.11.30 21:00'

	months = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月']
	# def __init__(self, arg):
	# 	super(Analyse, self).__init__()
	# 	self.arg = arg

	def __init__(self):
		pass

	def sum_year_count(self,filename):
		""" 一年的更新字数"""
		sum = 0
		with open(filename) as f:
			f_reader = csv.reader(f)
			for row  in f_reader:
				sum += int(row[1])
		print(sum)
		return sum


	def every_month_count(self,filename):
		"""每月更新字数，返回一个列表"""
		res = []
		with open(filename) as f:
			f_csv = csv.reader(f)
			temp_month = '2018-01'
			month_count = 0
			sum_all = 0 
			for row in f_csv:
				sum_all += int(row[1])
				if  row[2].startswith(temp_month):
					month_count += int(row[1])
				else:
					res.append(month_count)
					month_count = 0
					temp_month = row[2][:7]
					month_count += int(row[1])
				# print(res)
		sum = 0
		for x in res:
			sum += x
		
		res.append(sum_all - sum)
		# print('final')
		# print(res)
		return res

	################### render ####################
	def render_average_day(self):
		"""2018年平均每天更新字数"""
		# configure(global_theme='essos')

		bar = Bar(self.title,self.subtitle,width=1200)
		# bar.use_theme('dark')

		authors = []
		one_years_all = []
		for info in self.allinfo:
			authors.append(info[0])
			one_years_all.append(self.sum_year_count(info[1]))

		every_day = [int(x / (365 - 31)) for x in one_years_all]
		print(authors,every_day)

		bar.add("2018年平均每天更新字数",
				authors,
				every_day,
				is_label_show=True,
				label_pos='inside'
				)
		bar.render('2018年平均每天更新字数.html')


	def render_all_year(self):
		"""2018年总更新字数"""
		bar = Bar(self.title,self.subtitle,width=1200)
		authors = []
		one_years_all = []
		for info in self.allinfo:
			authors.append(info[0])
			one_years_all.append(self.sum_year_count(info[1]))

		one_years_all = [int(x / 10000) for x in one_years_all]
		bar.add('2018年总更新字数,单位（万字）',
				authors,
				one_years_all,
				is_label_show=True,
				label_pos='inside'
				)
		bar.render('2018年总更新字数.html')



	def render_every_month_down(self):
		info = self.allinfo[0]
		# bar = Bar('','2018年下半年每月更新字数,单位（万字）' + self.title)
		bar = Bar('2018年下半年每月更新字数,单位（万字）' + self.title,title_top='bottom')

		# bar = Bar('2018年下半年每月更新字数,单位（万字）' ,self.subtitle + ' ' + self.title,title_top='bottom')
		for info in self.allinfo:
			author = info[0]
			filename = info[1]
			months = self.every_month_count(filename)
			new_months = [int(x / 1000) / 10  for x in months]
			# print(author)
			# print(new_months)
			# print(new_months[6:])
			# print(self.months[6:])

			
			bar.add(author,
					self.months[6:],
					new_months[6:],
					is_label_show=True
					)
		bar.render('2018年下半年每月更新字数.html')

	def render_every_month_up(self):
		info = self.allinfo[0]
		# bar = Bar('','2018年下半年每月更新字数,单位（万字）' + self.title)
		bar = Bar('2018年上半年每月更新字数,单位（万字）' + self.title,title_top='bottom')

		# bar = Bar('2018年下半年每月更新字数,单位（万字）' ,self.subtitle + ' ' + self.title,title_top='bottom')
		for info in self.allinfo:
			author = info[0]
			filename = info[1]
			months = self.every_month_count(filename)
			new_months = [int(x / 1000) / 10  for x in months]
			# print(author)
			# print(new_months)
			# print(new_months[6:])
			# print(self.months[6:])

			
			bar.add(author,
					self.months[:6],
					new_months[:6],
					is_label_show=True
					)
		bar.render('2018年上半年每月更新字数.html')


if __name__ == '__main__':
	configure(global_theme='dark')

	analyse = Analyse()
	analyse.render_average_day()
	analyse.render_all_year()
	analyse.render_every_month_down()
	analyse.render_every_month_up()


