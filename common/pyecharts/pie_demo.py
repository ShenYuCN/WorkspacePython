from pyecharts import Pie

# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图示例",title_pos = "right")
# pie.add("", attr, v1,  radius=[40, 75],is_label_show=True)
# pie.render()


attr = ["一月","二月","三月"]
v1 = [10,20,30]
pie = Pie("饼图")
pie.add("",
	attr,
	v1,
	radius = [40,80],
	is_label_show = True)
pie.render()


