import re
'''
. 除换行符之外的任意字符
？ 0或1个
+  1或多个
*  0或多个


'''

# 截取双引号内的内容
newStrip = 'aaa"bbb" ccc"ddd"eee'
pattern = re.compile('["](.*?)["]')
print(pattern.findall(newStrip))
# ['bbb', 'ddd']



string222 = 'adcd<user@test.com>'
# pattern222 = re.compile('<([^>]+)')
pattern222 = re.compile('<(.+)>')
print(pattern222.findall(string222))
# ['user@test.com']




string333 = 'aaaaa2002年的第五场雪bbbb'
pattern333 = re.compile('第(.*)场雪')
print(pattern333.findall(string333))
# ['五']



string444 = 'frameworkPayload/THAppModule_Example.app/Frameworks/THSmartCustomServiceModule.framework/JSCSLocalizable.bundle/'
pattern444 = re.compile('Frameworks/(.*).framework')
print(pattern444.findall(string444))
# ['THSmartCustomServiceModule']




# 取出html中的歌手名和歌名
'''<div id="songs-list">
	<h2 class="title">经典老歌</h2>
	<p class="introduction">
		经典老歌列表
	</p>
	<ul id="list" class="list-group">
		<li data-view="2">一路上有你</li>
		<li data-view="7">
			<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
		</li>
		<li data-view="4" class="active">
			<a href="/3.mp3" singer="齐秦">往事随风</a>
		</li>
		<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
		<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
		<li data-view="5">
			<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
		</li>
	</ul>
</div>'''
html = open('html.py').read()

# 使用search
result = re.search(r'<a.*?singer="(.*?)">(.*?)</a>',html)
# 歌手名和歌名都在<a>标签中, 从 <a 开始匹配
if result:
	print(result.group(1), result.group(2))

# 输出结果
# 任贤齐 沧海一声笑   
# search只能返回匹配到的第一个结果



# 使用findall
result = re.findall('<a.*?singer="(.*?)">(.*?)</a>', html)
if result:
	print(result)

# 输出结果
# [('任贤齐', '沧海一声笑'), ('齐秦', '往事随风'), ('beyond', '光辉岁月'), 
# ('陈慧琳', '记事本'), ('邓丽君', '但愿人长久')]
# findall会返回所有匹配的字符串的list

	