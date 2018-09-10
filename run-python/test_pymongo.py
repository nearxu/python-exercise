#!/usr/bin/python
# -*-coding:utf-8 -*-

# https://github.com/nummy/pymongo-tutorial-cn

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 获取数据库
db = myclient['lists']

# dblist = myclient.database_names()
# if "test" in dblist:
#     print("数据库已存在！")

# 获取集合
posts = db.bears

# mylist = {"name": "Lucy", "sex": "female", "job": "nurse"}

# post = {"author": "Maxsu",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"]
# 插入文档
# collection.insert_one(mylist)
# posts.insert(post)
# users = collection.find_one()

# 查找文档
for item in posts.find():
    print(item, 'items')
