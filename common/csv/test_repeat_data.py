import csv


# 读取文件
with open('maoyan.csv') as f:
    with open('maoyan.csv','rb') as in_file, open('maoyan_no_repeat.csv','wb',encoding = 'utf-8-sig') as out_file:
        seen=set()
        for line in in_file:
            print(line)
            if line in seen:
	            out_file.write(line)
            else:
	            seen.add(line)
	            print(seen)


