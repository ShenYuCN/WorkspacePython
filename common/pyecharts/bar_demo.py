from pyecharts import Bar
from pyecharts import configure


configure(global_theme = 'dark')
# bar = Bar("我的第一个图表", "这里是副标题")
# # bar.use_theme('vintage')

# bar.add("服装", 
# 	["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], 
# 	[5, 20, 36, 10, 75, 90]
# 	)
# # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# bar.render()    # 生成本地 HTML 文件


# bar = Bar('Title','SubTitle')
# bar.add('服装',['a','b','c'],[5,20,50])
# bar.render()

# Bar('示例').add('中间的',['a','b','c'],[5,20,50]).render()



CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
clothes_v1 = [5, 20, 36, 10, 75, 90]
clothes_v2 = [10, 25, 8, 60, 20, 80]


(Bar("柱状图数据堆叠示例")
    .add("商家A", CLOTHES, clothes_v1, is_label_show=True)
    .add("商家B", CLOTHES, clothes_v2, is_label_show=True)
    .render())

# (Bar("柱状图数据堆叠示例")
#     .add("商家A", CLOTHES, clothes_v1, is_stack=True)
#     .add("商家B", CLOTHES, clothes_v2, is_stack=True)
#     .render())
