#!/usr/bin/env python
# coding=utf-8

import json
import csv

data = [{
    'name': '小胖',
    'gender': '男',
    'birthday': '1999-10-10',
}]

# Python内置的open()函数打开一个文件，创建一个file对象
# w 打开一个文件只用于写 w+ 该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除
# r r+ 以只读方式打开文件 这是默认模式
# with open('./data.json', 'w', encoding='utf-8') as fp:
#     fp.write(json.dumps(data, ensure_ascii=False))


# with open('./list.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     writer.writerow(['id', 'name', 'score'])
#     writer.writerow(['1001', 'kb', '99'])
#     writer.writerow(['1002', 'www', '90'])
#     writer.writerow(['1003', 'pp', '56'])
#     writer.writerows([['1004', 'mm', '60'], ['1005', 'nn', '70']])

# with open('./list.csv', 'r') as fp:
#     reader = csv.reader(fp)
#     for row in reader:
#         print(row)

# # dict write

# with open('./dict.csv', 'w') as csvfile:
#     fields = ['name', 'age', 'likes']
#     writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=' ')
#     writer.writeheader()
#     writer.writerow({'name': 'zhu', 'age': '12', 'likes': '屎'})
#     writer.writerow({'name': 'dog', 'age': '11', 'likes': '屎'})
#     writer.writerows([{'name': 'aa', 'age': '11', 'likes': 'assa'}, {
#                      'name': 'qqq', 'age': '2', 'likes': 'aaa'}])

with open('./dict.csv', 'r') as fp:
    fields = ['name', 'age', 'likes']
    reader = csv.DictReader(fp)
    for row in reader:
        print(row)
