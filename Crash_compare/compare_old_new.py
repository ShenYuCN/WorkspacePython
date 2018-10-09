
'''

前提： installed_modules   framework_list_aready_download  为标准json，防止和该文件一个平级目录

优点：  对比本版和上一版的配置，增量更新需要的framework，如果没有更新，那么使用上次的，一个都不需要下载和压缩

1. 取出 ipa 里面 frameworks 里面的所有framworks， 可能新版本会增加新的framework    --->  list
2. 将第一步取出来的framework列表，在 installed_modules 里面读出这个列表里的framework对应的版本号  --->  list
3. 第二步取出来的list 和 framework_list_aready_download 内容做对比
	3.1 最简单的对比就是读2个文件成字符串，然后匹配对比
	3.2 读出不一样的版本，然后打印出来不一样的framework


ibiu下载frameworks有2种：
	1、biu -d JDDBaseModule_1.1.12   （一次一个）
	2、biu -dsym  读取 framework_list 里面的配置表下载 （多个同时下载）

'''

import zipfile
import re
import simplejson
import sys



def findAllFrameworks(ipa_path):
	"""
	findAllFrameworks----adb
	"""
	# ipa_path = 'test.ipa'
	ipa_file = zipfile.ZipFile(ipa_path)
	# print(ipa_file)
	name_list = ipa_file.namelist()
	# ['Payload/', 'Payload/THAppModule_Example.app/', Payload/THAppModule_Example.app/Frameworks/THSmartCustomServiceModule.framework/JSCSLocalizable.bundle/'

	frameworks = []
	for path in name_list:
		pattern = re.compile('Frameworks/(.*).framework')
		tempList = pattern.findall(path)
		if len(tempList) > 0 and not tempList[0] in frameworks:
			# print(tempList[0])
			frameworks.append(tempList[0])
	return frameworks


def findVersionsInNewIpa(frameworks):
	# frameworks = ['JDBFoundationModule', 'JDBTrackModule', 'JDDBaseModule', 'JDDThirdPartModule', 'JDTAFNetworkingModule', 'JDTOpenUDIDModule', 'JDTYYModel', 'THSmartCustomServiceModule','THUIKitConfigModule']
	file_new = open('installed_modules').read()
	dict_new = jsonToDict_two(file_new)
	# print('dict_new=====', dict_new)
	# print(dict_new['JDTAFNetworkingModule'])

	file_old = open('framework_list_aready_download').read()
	dict_old = jsonToDict_two(file_old)
	# print('dict_old=====', dict_old)
	# print(dict_old['JDTAFNetworkingModule'])

	# TODO:最后测试新加framework，旧版本没有的情况
	tuple_list = []
	for framework in frameworks:
		if framework in dict_new:
			version_new = dict_new[framework]
			version_old = dict_old.get(framework, 'not exist')
			tuple_list.append((framework, version_new, version_old))

	# print('tuple_list====', tuple_list)

	for new_old in tuple_list:
		if not new_old[1] == new_old[2]:
			print('%-30s' % new_old[0], '   新版本:', '%-9s' %
				  new_old[1], '   旧版本:', new_old[2])


def jsonToDict_one(json):
	return eval(json)


def jsonToDict_two(json):
	return simplejson.loads(json)
	# ret_dict = simplejson.loads(json_str)
	# 字典到JSON转化：
	# json_str = simplejson.dumps(dict)


if __name__ == '__main__':
	args = sys.argv
	# print(args)
	if len(args) < 2 or not args[1].endswith('.ipa'):
		print('Usage: python3 compare.py  /path/to/.ipa')
		sys.exit()

	frameworks = findAllFrameworks(args[1])
	# print(frameworks)
	versions = findVersionsInNewIpa(frameworks)
