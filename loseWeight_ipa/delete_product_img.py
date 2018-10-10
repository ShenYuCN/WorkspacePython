import shutil
import os



for line in open('product_imgs'):
	if line.strip().endswith('.png'):


		# 删除 product_imgs 中 PD/PDResources/ 的文件
		PD_PDResources_file_dir = '/Users/happiness/Documents/Files/JD-Thailand/Thailand-ProductDetail/THProductDetailModule/THProductDetailModule/Classes/PD/PDResources/'
		file_path = PD_PDResources_file_dir + line.strip().split('/')[-1]	
		if os.path.exists(file_path):
			os.remove(file_path)


		# 删除 PD/PDResources/ 合并到asset 目录产生的 -2 -1 重复文件夹
		asset_dir = '/Users/happiness/Documents/Files/JD-Thailand/Thailand-ProductDetail/THProductDetailModule/THProductDetailModule/Assets/Resources.xcassets'
		for root,dir,files in  os.walk(asset_dir):
			# print(root,'  ',dir,'   ',files)
			# /Users/happiness/Documents/Files/JD-Thailand/Thailand-ProductDetail/THProductDetailModule/THProductDetailModule/Assets/Resources.xcassets/shareorder_video.imageset    []     ['Contents.json', 'shareorder_video@2x.png']
			last_path = root.split('/')[-1]
			# print(last_path)
			if last_path.split('.')[0].endswith('-1') or last_path.split('.')[0].endswith('-2'):
				shutil.rmtree(root)
		

			# 删除空文件夹
			if not os.listdir(root):
				print('目录为空,删除',root)
				os.rmdir(root)


		# 删除 product_imgs 中 Resources.xcassets 的文件
