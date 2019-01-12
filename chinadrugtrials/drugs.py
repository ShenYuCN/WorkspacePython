import re

file = open('dmo1.html').read()
# file = open('demo.html').read()
# print(file)

# pattern = re.compile('data-original="(.*?)\salt="(.*?)"')


# result = pattern.search(file)
# print(result.group())

# print('0   ' + result.group(0))
# print('1   '+result.group(1))
# print('2   '+result.group(2))



mlist = []
pattern_date = re.compile('首次公示信息日期：.*?<td>(.*?)</td>',re.DOTALL)
date = pattern_date.search(file)
mlist.append(date.group(1).strip())


# pattern = re.compile('首次公示信息日期：.*?<td>.*?(.*?).*?</td>.*?登记号：.*?FFFFFF">(.*?)</td>.*?适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)
# pattern = re.compile('登记号：.*?FFFFFF">(.*?)</td>.*?适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)



pattern_code = re.compile('登记号：.*?FFFFFF">(.*?)</td>',re.DOTALL)
code = pattern_code.search(file)
mlist.append(code.group(1).strip())


# pattern = re.compile('登记号：.*?FFFFFF">(.*?)</td>',re.DOTALL)


pattern_func = re.compile('适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)
func = pattern_func.search(file)
mlist.append(func.group(1).strip())




# pattern = re.compile('适应症：.*?FFFFFF">(.*?)</td>',re.DOTALL)
# result = pattern.search(file)

# print(result.groups())

# print('1   '+result.group(1))
# print(result.group(1).strip())
# print('2   '+result.group(2))

# print('3   '+result.group(3))

# print(mlist)


pattern_author = re.compile('单位名称.*?#FFFFFF">(.*?)</td>',re.DOTALL)
result = pattern_author.search(file)


for info in pattern_author.findall(file):
	mlist.append(info.strip())
	# print(info.strip())


# print(result.groups())

# print(result.group(1).strip())

# mlist.append(author.group(1).strip())

								          	

pattern_author_sub = re.compile('<td align="center">.*?<td align="left" height="30">(.*?)</.*?<td align="left">',re.DOTALL)
# author_sub = pattern_author.search(file)


for info in pattern_author_sub.findall(file):
	mlist.append(info.strip())
	# print(info.strip())

	# mlist.append(info.strip())




print(mlist)




