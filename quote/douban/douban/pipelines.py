# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class DoubanPipeline(object):
    def __init__(self,host,port,dbname):
        client = pymongo.MongoClient(host=host,port=port)
        db = client[dbname]
        self.post = db[dbname]

    def process_item(self, item, spider):
        appInfo = dict(item)
        self.post.update({'ranking':item['ranking']},{'$set':dict(item)},True)
        return item

    @classmethod
    def from_settings(cls,settings):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        print(host, port, dbname,'++++++++++++++++++++++++++++++++++')
        return cls(host, port, dbname)