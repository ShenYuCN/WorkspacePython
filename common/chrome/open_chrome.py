import webbrowser

url = 'http://wwww.baidu.com'
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# webbrowser.get(chrome_path).open(url)

# webbrowser.open(url, new=0, autoraise=True)
# 用默认浏览器打开url, new=0是当前窗口, 1: 新窗口, 2: 新tab.  
# autoraise 可能是自动切换到浏览器..测试无效. 最常用函数.

webbrowser.open(url,new = 1)