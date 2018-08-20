newfile = open('软件工程名单.txt','w')
girls = open('晋城校区女生名单.txt','w')
girlsInSoftware = open('软件工程女生名单.txt','w')

num = 0
girlNum = 0
girlsInSoftNum = 0
for line in open('1.txt'):
	if line.endswith('软件工程\n') == True:
		num = num +1
		newfile.write(line)
		pass

	if '女' in line:
		girlNum = girlNum + 1
		girls.write(line)
		pass

	if '女' in line and line.endswith('软件工程\n') == True:
		girlsInSoftNum = girlsInSoftNum + 1
		girlsInSoftware.write(line)
		pass

newfile.write('\n软件工程专业学生数量:' + str(num))
newfile.close()

girls.write('\n晋城校区女生数量:' + str(girlNum))
girls.close()

girlsInSoftware.write('\n软件工程女生数量:' + str(girlsInSoftNum))
girlsInSoftware.close()

print(allnum)