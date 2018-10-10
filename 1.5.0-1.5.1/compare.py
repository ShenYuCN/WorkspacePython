old = open('1.5.0_installed_modules.txt').read()
# print(dict(old))
older = old[1:len(old)-2]
# print(older)
oldList = older.split(',')
print(oldList)
print('长度'+ str(len(oldList)))
print(oldList[0])