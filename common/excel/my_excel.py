
#!/usr/bin/env python
# coding=utf-8
 
from xlwt import *
#需要xlwt库的支持
#import xlwt
file = Workbook(encoding = 'utf-8')
#指定file以utf-8的格式打开
table = file.add_sheet('shenyu')
#指定打开的文件名
 
data = {
        "3":["王五",60,66,68],
        "1":["张三",150,120,100],
        "2":["李四",90,99,95]
      
        }
#字典数据
 
ldata = []
num = [a for a in data]
#for循环指定取出key值存入num中
print('original',num)

num.sort()
#字典数据取出后无需，需要先排序
 
print('sorted',num)

for x in num:
#for循环将data字典中的键和值分批的保存在ldata中
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)
    print('ldata',ldata)
 
for i,p in enumerate(ldata):
    print('i',i,'p',p)
#将数据写入文件,i是enumerate()函数返回的序号数
    for j,q in enumerate(p):
        print('j',j,'q',q)
        table.write(i,j,q)
file.save('data.xls')
