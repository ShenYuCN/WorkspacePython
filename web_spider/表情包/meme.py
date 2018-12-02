"""
爬表情包《同步》
meme  sticker

1. 抓取网页html
2. 截取对应图片的src
	2.1 使用正则截取
	2.2 BeautifulSoup
3. 下载存储图片


<a class="col-xs-6 col-sm-3" href="https://www.doutula.com/photo/1598057" style="padding:5px;">
<img class="gif" style="min-height: inherit;left: 5px;top:5px" src="//static.doutula.com/img/gif.png">
<img src="//static.doutula.com/img/loader.gif" style="width: 100%; 
height: 100%;" data-original="https://ws3.sinaimg.cn/bmiddle/9150e4e5gy1fx94ed1vybg201n01nq2r.gif" alt="动耳朵" class="img-responsive lazy image_dta" data-backup="http://img.doutula.com/production/uploads/image//2018/11/15/20181115293811_BAXqCL.gif!dta">
<p style="display: none">动耳朵</p>
</a>

"""

import requests
import re
import os
from bs4 import BeautifulSoup


IMAGE_FILE_PATH = "meme_images"


def get_url(url):
	file = requests.get(url)

	if not os.path.isdir(IMAGE_FILE_PATH):
		print('当前文件夹下  不存在meme_images目录，将要创建')
		os.makedirs(IMAGE_FILE_PATH)
	else:
		print('当前文件夹下  存在meme_images目录，无须创建')

	# 这里切换两种解析方式
	# parse_response_re(file.text)
	parse_response_beautifule_soup(file.text)


# 使用beautiful soup解析
def parse_response_beautifule_soup(conent):
	soup = BeautifulSoup(conent,'lxml')
	for img_code in soup.find_all('img'):
		if img_code.get('data-original') and img_code['alt']:
			img_url = img_code.get('data-original')
			img_name = img_code['alt'] + os.path.splitext(img_url)[1]
			download_save_image(img_url,img_name)




# 使用正则解析
def parse_response_re(content):
	# pattern = re.compile('data-original="(.*?)".*?alt="(.*?)"')
	pattern = re.compile('data-original="(.*?)"\salt="(.*?)"')
	# print(pattern.findall(file)) 
	# [('https://ws3.sinaimg.cn/bmiddle/9150e4e5gy1fx94kjw3zmg208c08cglz.gif', '然后？然后就没有然后了'), ('https://ws4.sinaimg.cn/bmiddle/9150e4e5gy1fx94ki1cy9g203c035wea.gif', '谁TM在放屁怎么这么臭')]

	for info in pattern.findall(content):
		download_save_image(info[0],info[1] + os.path.splitext(info[0])[1])

def download_save_image(image_url,image_name):
	print(image_url,image_name)
	image_respose = requests.get(image_url)
	name = IMAGE_FILE_PATH + '/' + image_name
	print(name)
	if image_respose.status_code == 200:
		open(name,'wb').write(image_respose.content)

if __name__ == '__main__':
	for x in range(1,2):
		url = 'https://www.doutula.com/photo/list/?page=%d' % x
		get_url(url)

