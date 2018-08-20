girls = open('晋城校区女生名单.txt','w')

girlNum = 0
for line in open('1.txt'):
	
	L = line.split('\t')
	print(L)

	if '女' in L:
		girlNum = girlNum + 1
		girls.write(line)
		pass


girls.write('\n晋城校区女生数量:' + str(girlNum))
girls.close()
