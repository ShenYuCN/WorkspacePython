import zipfile,re,simplejson


'''

优点：  只用关心本次发布的ipa，不用考虑上一版本的
1. 取出 ipa 里面 frameworks 里面的所有framworks， 可能新版本会增加新的framework    --->  list
2. 将第一步取出来的framework列表，在 installed_modules 里面读出这个列表里的framework对应的版本号  --->  list
3. 生成 framework_list 文件


ibiu下载frameworks有2种：
	1、biu -d JDDBaseModule_1.1.12   （一次一个）
	2、biu -dsym  读取 framework_list 里面的配置表下载 （多个同时下载）


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
	
def findVersionsInNewConfigFile(frameworks):
	# frameworks = ['JDBFoundationModule', 'JDBTrackModule', 'JDDBaseModule', 'JDDThirdPartModule', 'JDTAFNetworkingModule', 'JDTOpenUDIDModule', 'JDTYYModel', 'THSmartCustomServiceModule','THUIKitConfigModule']
	file_new = open('installed_modules').read()
	dict_new = simplejson.loads(file_new)

	framework_list = open('framework_list','w')

	for framework in frameworks:
		framework_list.write(framework+'_'+dict_new[framework]+'\n')

	framework_list.close()



if __name__ == '__main__':
	frameworks = findAllFrameworks()
	print(frameworks)
	findVersionsInNewConfigFile(frameworks)
    # args = sys.argv[1:]
    # if len(args) &lt; 1:
    #     print ('Usage: python3 ipaanalyze.py /path/to/ipa')
 
    # ipa_path = args[0]
    # analyze_ipa_with_plistlib(ipa_path)

    # find_plist_path(ipa_path)