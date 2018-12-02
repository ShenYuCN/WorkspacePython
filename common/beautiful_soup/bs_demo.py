from bs4 import BeautifulSoup




html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""




soup = BeautifulSoup(html_doc)

print(soup.find_all('a'))

for  link in soup.find_all('a'):
	print(link.get('href'))
	#或者下面这种方式，【】
	# print(link['href'])



html = """
<a class="col-xs-6 col-sm-3" href="https://www.doutula.com/photo/9173800" style="padding:5px;">
<img class="gif" style="min-height: inherit;left: 5px;top:5px" src="//static.doutula.com/img/gif.png">
 <img src="//static.doutula.com/img/loader.gif" style="width: 100%; height: 100%;" data-original="https://ws4.sinaimg.cn/bmiddle/9150e4e5gy1fx94e9ldc9g208c08cq2x.gif" alt="像我这样优秀的人不多啦" class="img-responsive lazy image_dta" data-backup="http://img.doutula.com/production/uploads/image//2018/11/15/20181115293811_lwsxHv.gif!dta">
<p style="display: none">像我这样优秀的人不多啦</p>
</a>

<a class="col-xs-6 col-sm-3" href="https://www.doutula.com/photo/4391584" style="padding:5px;">
<img class="gif" style="min-height: inherit;left: 5px;top:5px" src="//static.doutula.com/img/gif.png">
<img src="//static.doutula.com/img/loader.gif" style="width: 100%; height: 100%;" data-original="https://ws2.sinaimg.cn/bmiddle/9150e4e5gy1fx94ebmf1cg207o07m3z8.gif" alt="哼，傻逼" class="img-responsive lazy image_dta" data-backup="http://img.doutula.com/production/uploads/image//2018/11/15/20181115293811_bUsgFW.gif!dta">
<p style="display: none">哼，傻逼</p>
</a>
"""
soup_html = BeautifulSoup(html,'lxml')

for content in soup_html.find_all('img'):
	if content.get('data-original') and content.get('alt'):
		print(content.get('data-original'),content['alt'])
	
	














