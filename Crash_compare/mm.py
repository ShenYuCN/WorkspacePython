import zipfile,re,simplejson


'''
1. 取出 ipa 里面 frameworks 里面的所有framworks， 可能新版本会增加新的framework    --->  list
2. 将第一步取出来的framework列表，在 installed_modules 里面读出这个列表里的framework对应的版本号  --->  list
3. 第二步取出来的list 和 framework_list_aready_download 内容做对比
	3.1 最简单的对比就是读2个文件成字符串，然后匹配对比
	3.2 读出不一样的版本，然后打印出来不一样的framework
'''
def findAllFrameworks():
	ipa_path = 'test.ipa'
	ipa_file = zipfile.ZipFile(ipa_path)
	# print(ipa_file)
	name_list = ipa_file.namelist()
	# ['Payload/', 'Payload/THAppModule_Example.app/', Payload/THAppModule_Example.app/Frameworks/THSmartCustomServiceModule.framework/JSCSLocalizable.bundle/'

	frameworks = []
	for path in name_list:
		pattern = re.compile('Frameworks/(.*).framework')
		tempList =  pattern.findall(path)
		if len(tempList) > 0 and not tempList[0] in frameworks:
			# print(tempList[0])
			frameworks.append(tempList[0])
	return frameworks
	
def findVersionsInNewIpa(frameworks):
	print('new',frameworks)
	file = open('installed_modules').read()
	print('installed_modules',file)
	dictData = jsonToDict_two(file)
	print('dictdata',dictData)
	print(dictData['JDBUserManagerModule'])


def jsonToDict_one(json):
	return eval(json)

def jsonToDict_two(json):
	return simplejson.loads(json)
	# ret_dict = simplejson.loads(json_str)
	# 字典到JSON转化：
	# json_str = simplejson.dumps(dict)

if __name__ == '__main__':
	frameworks = findAllFrameworks()
	print(frameworks)
	versions = findVersionsInNewIpa(frameworks)
    # args = sys.argv[1:]
    # if len(args) &lt; 1:
    #     print ('Usage: python3 ipaanalyze.py /path/to/ipa')
 
    # ipa_path = args[0]
    # analyze_ipa_with_plistlib(ipa_path)

    # find_plist_path(ipa_path)