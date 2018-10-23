#!/usr/bin/env python
# coding=utf-8

# 先查索引,然后通过索引找到相应内容

mydict = {"name": "xiaoming"}

mydict['name'] = "xiaohong"

website = {1: "google", "second": "baidu", 3: "facebook", "twitter": 4}

print(website.keys())

print(website.values())

for key in website.keys():
    print(key, type(key))

# website.copy  website.pop('second')

print(website.copy(), website.pop('second'))

new = {
    'qq': 'first in cn',
    'python': 'qiwsir.github.io',
    'alibaba': 'Business'
}

print(website.update(new))