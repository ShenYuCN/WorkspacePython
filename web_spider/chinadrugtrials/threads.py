import requests
import time
from threading import Thread
from queue import Queue
import json

"""
requests库请求网页，获取json格式数据，解析字典提取我们要的信息，存储json文件
使用threading为网页请求部分设计多线程
使用两个队列，分别存储待抓取url和解析后的结果数据
拥有github账户，需要在代码中填入账号和密码
了解装饰器（这里只是计算运行时间，不了解也没关系）

爬虫说明如下
1.run_time函数是一个计算程序运行时间的装饰器，作用于Spider对象的run函数
2.Spider类


__init__初始化一些常量
produce_url用于生产所有URL，存储到Queue队列qurl中。5千多个元素分布在171个页面之中，将这171个URL存入队列中等待请求解析。其实这里不需要多线程之间通信，所以使用list代替Queue队列也是可以的。
get_info网页的请求与解析，之后开启多线程就是多个这个函数同时运行。函数逻辑：只要qurl中还有元素，就每次从qurl中提取一个url进行请求解析，将结果存入data列表中。当队列中没有元素了即退出循环（爬虫结束）。
run调用函数，运行爬虫。首先调用produce_url产生待爬URL队列。然后开启指定数量的线程，每个线程都从qurl不断提取URL进行解析，将数据存入data列表中。等到URL队列被解析结束，将data中的数据存储入json文件中
"""

def run_time(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print('running', end-start, 's')
    return wrapper


class Spider():

    def __init__(self):
        self.qurl = Queue()
        self.data = list()
        self.email = '' # 登录github用的邮箱
        self.password = '' # 登录github用的密码
        self.page_num = 171
        self.thread_num = 10

    def produce_url(self):
        baseurl = 'https://api.github.com/repos/python/cpython/forks?page={}'
        for i in range(1, self.page_num + 1):
            url = baseurl.format(i)
            self.qurl.put(url) # 生成URL存入队列，等待其他线程提取

    def get_info(self):
        while not self.qurl.empty(): # 保证url遍历结束后能退出线程
            url = self.qurl.get() # 从队列中获取URL
            print('crawling', url)
            req = requests.get(url, auth = (self.email, self.password))
            data = req.json()
            for datai in data:
                result = {
                    'project_name': datai['full_name'],
                    'project_url': datai['html_url'],
                    'project_api_url': datai['url'],
                    'star_count': datai['stargazers_count']
                }
                self.data.append(result)

    @run_time
    def run(self):
        self.produce_url()

        ths = []
        for _ in range(self.thread_num):
            th = Thread(target=self.get_info)
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

        s = json.dumps(self.data, ensure_ascii=False, indent=4)
        with open('github_thread.json', 'w', encoding='utf-8') as f:
            f.write(s)

        print('Data crawling is finished.')

if __name__ == '__main__':
    Spider().run()
