from time import sleep
import os,shutil
usb_path = '/Volumes'
content = os.listdir(usb_path) # 返回路径下所有文件以及文件夹的名称
# ['Macintosh HD', 'MobileBackups', 'T']

while True:
	new_content = os.listdir(usb_path)
	if new_content != content:
		print('U盘插入了')
		break;
	print('等3秒')	
	sleep(3)

x = [item for item in new_content if item not in content]  #找到磁盘

print(x)
shutil.copytree(os.path.join(usb_path,x[0]),'/User/home/usb-copy')