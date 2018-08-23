import os


'''

优点：  只用关心本次发布的ipa，不用考虑上一版本的
1. 取出 ipa 里面 frameworks 里面的所有framworks， 可能新版本会增加新的framework    --->  list
2. 将第一步取出来的framework列表，在 installed_modules 里面读出这个列表里的framework对应的版本号  --->  list
3. 生成 framework_list 文件


ibiu下载frameworks有2种：
	1、biu -d JDDBaseModule_1.1.12   （一次一个）
	2、biu -dsym  读取 framework_list 里面的配置表下载 （多个同时下载）


'''
def remove_not_zip_file():
	top = '/Users/happiness/Documents/WorkspacePython/Crash_compare/dsyms'
	for root,dirs,files in os.walk(top):
		for name in files:
			print(name)
			if not name.endswith('.dSYM'):
				os.remove(os.path.join(root,name))
				



if __name__ == '__main__':
	remove_not_zip_file()
	# frameworks = findAllFrameworks()
	# print(frameworks)
	# findVersionsInNewConfigFile(frameworks)
	