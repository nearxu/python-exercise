# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

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
