from xlwt import *
file = Workbook(encoding='utf-8')
table = file.add_sheet('sheet')

table.col(0).width = 256 * 25
table.col(1).width = 256 * 30


# 后缀只有3种 @2x.png .imageset .gif, .png

# 新建一个数组，用来排序excel
res = [] 

file_product = open('product_imgs','w')
for line in open('image_delete.txt'):
	componentList = line.strip().split('/')
	imageName = ''
	if componentList[-1].endswith('.imageset'):
		imageName = componentList[-1].replace('.imageset','')
	elif componentList[-1].endswith('@2x.png'):
		imageName = componentList[-1].replace('@2x.png','')
	elif componentList[-1].endswith('@3x.png'):
		imageName = componentList[-1].replace('@3x.png','')
	elif componentList[-1].endswith('.png'):
		imageName = componentList[-1].replace('.png','')
	elif componentList[-1].endswith('.gif'):
		imageName = componentList[-1].replace('.gif','')

	res.append([componentList[1],imageName])

	if componentList[1] == 'THProductDetailModule':
		file_product.write(line)


file_product.close()

rows = 0
namesAll = []
namesKeys = []
for item in sorted(res,reverse = True):
	table.write(rows,0,item[0])
	table.write(rows,1,item[1])
	rows += 1

	namesAll.append(item[0])
	if not item[0] in namesKeys:
		namesKeys.append(item[0])




table.write(2,3,'模块名称')
table.write(2,4,'图片数量')

# cart  66个  
index = 3
for name in namesKeys:
	tempCount = namesAll.count(name)
	table.write(index,3,name)
	table.write(index,4,tempCount)
	index += 1



file.save('images_to_delete.xls')









