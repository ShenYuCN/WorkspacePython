import re
for line in open('test'):
	a = line.strip()
	print('a',a)

	pattern = re.compile('[""](.*?)["]')
	keys = pattern.findall(line.strip())
	print(keys)


	
	'''
	b = a[4 : -1]
	print('b',b)
	f = b.replace('章 ','章')
	print('f',f)

	c = f.replace(' ',',')
	print('c',c)
	d = c.replace('=',':')
	print('d',d)
	#  class:"chapterBean",chapterId:"42297301",chapterName:"第三百三十七章拳头太硬，罚酒好喝",chapterLevel:"1",wordNum:"8256",updateTime:"1531308963000"

	

	keyValesList = d.split(',')
	print('keyValesList',keyValesList)
	#  ['class:"chapterBean"', 'chapterId:"42297301"', 'chapterName:"第三百三十七章拳头太硬，罚酒好喝"', 'chapterLevel:"1"', 'wordNum:"8256"', 'updateTime:"1531308963000"']

	tmpList = ['class','chapterId','chapterName','chapterLevel','wordNum','updateTime']


	for i in range(len(keyValesList)):

		if tmpList[i] in keyValesList[i]:
			tempStr = '\"'+tmpList[i]+'\"'
			print('tempStr',tempStr)
			keyValesList[i] = keyValesList[i].replace(tmpList[i],tempStr)
			# finalStr.append(keyValesList[i])
			
	
	print('keyValesList',keyValesList)
	
	# print(finalStr)
	'''