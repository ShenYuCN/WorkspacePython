
import csv
headers = ['Symbol','Price','Date']
rows = [('AA', 39.48, '6/11/2007'),
         ('AIG', 71.38, '6/11/2007'),
         ('AXP', 62.58, '6/11/2007')
       ]



# 写入文件  
with open('aaa.csv','w') as f:
	f_csv = csv.writer(f)
	f_csv.writerow(headers)
	f_csv.writerows(rows)


# 读取文件
with open('aaa.csv') as f:
	f_csv_reader = csv.reader(f)
	print(f_csv_reader)
	#  两种方式，一种转换成list,一种for循环来
	# 要注意的是，f_csv_reader 只能被遍历一次。由于f_csv_reader 是可迭代对象，可以使用next方法一次获取一行。
	# print(list(f_csv_reader))

	for row in f_csv_reader:
		print(f_csv_reader.line_num,row) # line_num 从 1 开始




####  dict 相关


headers_dict = ['name', 'age']

datas_dict = [{'name':'Bob', 'age':23},
        {'name':'Jerry', 'age':44},
        {'name':'Tom', 'age':15}
        ]

#  写入文件
with open('dict.csv','w') as f:
	writer = csv.DictWriter(f, headers_dict)
	writer.writeheader()
	writer.writerows(datas_dict)


# 读取文件
with open('dict.csv') as f:
	reader = csv.DictReader(f)
	# print(list(reader))
	for row in reader:
		print(row['name'],row['age'])










