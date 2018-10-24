
#!/usr/bin/env python
# coding=utf-8

# json模块主要有四个比较重要的函数，分别是：

# - dump - 将Python对象按照JSON格式序列化到文件中
# - dumps - 将Python对象处理成JSON格式的字符串
# - load - 将文件中的JSON数据反序列化成对象
# - loads - 将字符串的内容反序列化成Python对象

import requests
import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('data save')


def main2():
    try:
        with open('data.json', 'r', encoding='utf-8')as fp:
            data = fp.read()
            print(data)
            data1 = data.split(',')
            print(data1)
            obj = {}
            for key in data1:
                obj
    except IOError as e:
        print(e)


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
}


def main3():
    response = requests.get(
        'http://api.tianapi.com/guonei/?key=APIKey&num=10', headers=headers)
    data = json.loads(response.text)
    print(data, type(data))
    # for news in data['newslist']:
    #     print(news['title'])


main3()
