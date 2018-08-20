import re
parametersNamesStr = open('ParameterNames.txt').read()
for line in open('PDMTAManager.m'):
	newStrip = line.lstrip()
	if newStrip.startswith('//') == False:
		pattern = re.compile('["](.*?)["]')
 		# keys = pattern.findall(newStrip)
 		# print(keys)
		print(pattern.findall(newStrip))
		pass

