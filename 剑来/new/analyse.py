from pyecharts import Bar
from pyecharts import configure
import csv





def sum_year_count(name):
	sum = 0
	with open(name) as f:
		f_reader = csv.reader(f)
		for row  in f_reader:
			sum += int(row[1])
	print(sum)
	return sum

if __name__ == '__main__':
	sum_count_jianlai = sum_year_count('jianlai.csv')
	sum_count_chendong = sum_year_count('chendong.csv')
	sum_count_maoni = sum_year_count('maoni.csv')

	configure(global_theme = 'dark')
	bar = Bar("贴吧@桑桑好桑心", "数据整理自起点和纵横，截止2018.11.30 21:00")
	# bar.use_theme('essos')

	# bar.add("2018年平均每天更新字数", 
	# 	["辰东", "总管", "猫腻"], 
	# 	[count_jianlai, count_chendong, count_maoni],
	# 	is_label_show=True
	# 	)


	authers = ["辰东", "总管", "猫腻"]
	sum_year_original = [sum_count_chendong,sum_count_jianlai,sum_count_maoni]
	print(sum_year_original)
	average_day = [int(x / (365 - 31)) for x in sum_year_original]
	sum_year = [int(x / 10000) for x in sum_year_original]
	print(sum_year)

	# bar.add(
	# 	"2018年平均每天更新字数", 
	# 	authers,
	# 	average_day, 
	# 	is_label_show=True
	# )
	bar.add(
		"2018年总共更新字数,单位（万字）",
		authers,
		sum_year,
		is_label_show=True,
		is_stack=True,
		label_pos="inside"
	)

	bar.render()    # 生成本地 HTML 文件
