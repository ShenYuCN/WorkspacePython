from pyecharts import Bar
from pyecharts import configure
import csv




class Analyse(object):
	"""网络小说作者2018年更新分析"""

	allinfo = [
				('辰东-圣墟','chendong.csv'),
				('总管-剑来','jianlai.csv'),
				('猫腻-大道朝天','maoni.csv')
				]

	title = '贴吧@桑桑好桑心'
	subtitle = '数据整理自起点和纵横，截止2018.11.30 21:00'

	months = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月']
	# def __init__(self, arg):
	# 	super(Analyse, self).__init__()
	# 	self.arg = arg

	def __init__(self):
		pass

	def sum_year_count(self,filename):
		""" 一年的更新字数 """
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
				print(row)
				sum_all += int(row[1])
				if  row[2].startswith(temp_month):
					month_count += int(row[1])
				else:
					res.append(month_count)
					month_count = 0
					temp_month = row[2][:7]
					month_count += int(row[1])
		sum = 0
		for x in res:
			sum += x
		
		res.append(sum_all - sum)
		print(res)

	def render_average_day(self):
		"""2018年平均每天更新字数"""
		# configure(global_theme='essos')

		bar = Bar(self.title,self.subtitle)
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
		bar = Bar(self.title,self.subtitle)
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

		self.every_month_count('jianlai.csv')

if __name__ == '__main__':
	configure(global_theme='dark')

	analyse = Analyse()
	# analyse.render_average_day()
	analyse.render_all_year()

