from pyecharts import Bar
from pyecharts import configure


configure(global_theme = 'dark')
bar = Bar("贴吧@桑桑好桑心", "数据整理自起点和纵横，截止至2018.11.30 21:00")
# bar.use_theme('essos')

bar.add("2018年平均  每天  更新字数", 
	["辰东", "总管", "猫腻", "裤子", "高跟鞋", "袜子"], 
	[5, 20, 36, 10, 75, 90]
	)
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render()    # 生成本地 HTML 文件



def average_day_count(name):
	for line in open(name,encoding = 'gbk'):
		print(line)

	return 10

if __name__ == '__main__':
	count = average_day_count('jianlai.csv')
	print(count)