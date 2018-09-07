#!/usr/bin/python
# -*- encoding:utf-8 -*-
 
"""
@author : kelvin
@file : mafengwo_scrapy
@time : 2017/2/21 7:50
@description : 爬蚂蜂窝热门旅游景点信息
"""
 
import requests
import json
import lxml.html
import csv
import sys
 
# 注意要先设置编译环境的默认编码形式为utf-8 ， 不然会报unicodeerror
# reload(sys)
# sys.setdefaultencoding('utf-8')
 
 
# data = {
#         "mddid": "21536",
#         "page": str(1)
#     }
# response = requests.post("http://www.mafengwo.cn/mdd/base/list/pagedata_citylist", data=data)
# print response.text
 
# 先创建一个csv文件，写好头部
with open("mafengwo_place.csv", 'w') as filed:  # a+为添加，w为擦除重写
    csv_writer = csv.DictWriter(filed, [
        '地名',
        '英文地名',
        '去过人数',
        '描述',
        '当地top1',
        '当地top2',
        '当地top3'
    ])
    csv_writer.writeheader()
 
 
def scrap_the_page(response):
    result = {}
    dic = json.loads(response.text)  # loads将json转为python对象
    content = dic['list']
    html = lxml.html.fromstring(content)   # 将json信息渲染成html
    for item in html.cssselect("li.item"):
        # 找出景点名
        result['name'] = item.cssselect("div.title")[0].text.strip()
        # 景点的英文名
        result['en_name'] = item.cssselect("p")[0].text
        # 多少人去过
        result['have_been'] = item.cssselect("b")[0].text_content()
        # 景点描述
        result['detail'] = item.cssselect("div.detail")[0].text.strip()
        # Top3
        # css选择器可以跨标签寻找节点
 
        top3 = item.cssselect("dd a")
        if len(top3) == 0:             # 处理这一块没有缺失信息的，有好几种情况
            result['top_1'] = ' '
            result['top_2'] = ' '
            result['top_3'] = ' '
        else:
            if len(top3) == 3:
                result['top_1'] = top3[0].text
                result['top_2'] = top3[1].text
                result['top_3'] = top3[2].text
            elif len(top3) == 2:
                result['top_1'] = top3[0].text
                result['top_2'] = top3[1].text
                result['top_3'] = ' '
            else:
                result['top_1'] = top3[0].text
                result['top_2'] = ' '
                result['top_3'] = ' '
 
            print(result)
            write_csv(result)
 
 
def write_csv(dict):
    with open("mafengwo_place.csv", 'a+') as f:  # a+为添加，w为擦除重写
        csv_write = csv.DictWriter(f, [
            '地名',
            '英文地名',
            '去过人数',
            '描述',
            '当地top1',
            '当地top2',
            '当地top3'
           ])
        csv_write.writerow({
            '地名':dict['name'],
            '英文地名':dict['en_name'],
            '去过人数':dict['have_been'],
            '描述':dict['detail'],
            '当地top1':dict['top_1'],
            '当地top2':dict['top_2'],
            '当地top3':dict['top_3']
        })
 
 
for page in range(1, 101):
    data = {
        "mddid": "21536",     # 通过post请求获得网页发送回来的信息
        "page": str(page)
    }
    response = requests.post("http://www.mafengwo.cn/mdd/base/list/pagedata_citylist", data=data)
    scrap_the_page(response)
