def sliceStr(mstring):
	res = []

	index = 0
	for x in range(1:len(mstring)):
		newStr = mstring[index : x+index]
		if checkStrIsOrNot(newStr):
			res.append(newStr)
		index += 1

		
	print(res)



def checkStrIsOrNot(partstr):
	index = 0
	while (index < (len(partstr) +1)/2):
		if partstr[index] != partstr[len[partstr] - 1 - index]:
			return false
		elif:
			index += 1

		
	return true

		
str = 'abfgfbcaaa'
sliceStr(str)