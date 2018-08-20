myfile = open('ParameterNames.txt','w')
nameList = []
for line in open('FIRParameterNames.h'):
	print(line)
	begin = line.find('@"')
	if begin > 0  and  line.startswith('///') == False:
		item = line[begin+2 : -3]
		print(item)
		nameList.append(item.upper())
		pass

print(nameList)
myfile.write(str(nameList))
myfile.close()


