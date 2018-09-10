#!/usr/bin/python
# -*-coding:utf-8 -*-

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client.db
collection = db["test"]
collection.insert({'name': 'aaa'})
