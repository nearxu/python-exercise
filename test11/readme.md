#https://zhuanlan.zhihu.com/p/24769534 #系列教程入门 #实现爬虫五门

### 关于爬取的数据存储到mongo

<!-- 1. settings.py
ITEM_PIPELINES = {
    'test11.pipelines.Test11Pipeline': 300,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "db"
MONGODB_COLLECTION = "test"

2. pipelines.py

import pymongo
from scrapy import log
from scrapy.conf import settings


class Test11Pipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client.db
        self.collection = db['test']

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
            if valid:
                self.collection.insert(dict(item))
                log.msg("Question added to MongoDB database!",
                        level=log.DEBUG, spider=spider)
        return item
 -->
