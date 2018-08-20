import re
# pattern = re.compile('"(.*)"')
pattern = re.compile('["](.*?)["]')

myStr = open('test.txt').read()
print pattern.findall(myStr)
