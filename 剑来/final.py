import re
import time
from xlwt import *

def getDataTime(timestamp):
	time_struct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d   %H:%M:%S',time_struct)

def getRowItems(rowStr):
	print('rowStr',rowStr)
	pattern = re.compile('["](.*?)["]')
	keys = pattern.findall(rowStr)
	print(keys)
	# ['chapterBean', '42297301', '第三百三十七章 拳头太硬，罚酒好喝', '1', '8256', '1531308963000']
	thatTime = getDataTime(int(keys[-1])/1000)
	rowItems = []
	rowItems.append(thatTime)

	orderAndName = keys[2].split(' ')
	rowItems.extend(orderAndName)

	rowItems.append(keys[-2])
	print('rowItems',rowItems)
	# ['2018-08-17   23:24:08', '第三百六十八章', '人间苦难说不得也', '14959']
	return rowItems
	
def setTableWidth(table):
	one_col = table.col(0)
	one_col.width = 256 * 21

	two_col = table.col(1)
	two_col.width = 256 * 8 *2

	three_col = table.col(2)
	three_col.width = 256 * 14 *2



file = Workbook(encoding = 'utf-8')
table = file.add_sheet('7月份至今')
setTableWidth(table)

row = 0
for line in open('0701'):
	rowItems = getRowItems(line.strip())
	for column,item in enumerate(rowItems):
		table.write(row,column,item)
	row +=1	
file.save('sword_arise.xls')