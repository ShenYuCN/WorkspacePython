'''
Created on Dec 24, 2012
将文件归档到zip文件，并从zip文件中读取数据
@author: liury_lab
'''

# 压缩成zip文件
from zipfile import *  
import os

my_dir = '/Users/happiness/Documents/WorkspacePython/common/zip/111/1.py'
# myzip = ZipFile(my_dir+'.zip', 'w', ZIP_DEFLATED)
# for file_name in os.listdir(my_dir):
#     file_path = my_dir + file_name
#     print(file_path)
#     myzip.write(file_path)
# myzip.close()

# print('finished')


 
f = ZipFile(my_dir +'.zip', 'w', ZIP_DEFLATED)
f.write(my_dir)
f.close()

# 从zip 文件中读取数据
# 直接检查一个zip格式的归档文件中部分或所有的文件，同时还要避免将这些文件展开到磁盘上
# my_zip = ZipFile('d:/中华十大名帖.zip')
# for file_name in my_zip.namelist():
#     print('File:', file_name, end = ' ')
#     file_bytes = my_zip.read(file_name)
#     print('has ', len(file_bytes), ' bytes')