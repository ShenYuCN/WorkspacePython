import os
import shutil
# my_file = '/Users/happiness/Documents/WorkspacePython/common/delete_file/1/aaa.py'
# if os.path.exists(my_file):
# 	os.remove(my_file)
# 	# os.unlink(my_file)
# else:
# 	print('TEST==== No such file or directory: %s'%my_file)



my_directory = '/Users/happiness/Documents/WorkspacePython/common/delete_file/1'


for root,dirs,files in  os.walk(my_directory,topdown = False):
	print(root,'    ',dirs,'    ',files)
	for name in files:
		print('file===',os.path.join(root,name))
		os.remove(os.path.join(root,name))
	for name in dirs:		
		print('dir===',os.path.join(root,name))
		os.rmdir(os.path.join(root,name))




shutil.rmtree(my_directory)