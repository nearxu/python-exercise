# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#Scrapy提供了 Item 类。 Item 对象是种简单的容器，保存了爬取到得数据。
# 其提供了 类似于词典(dictionary-like) 的API以及用于声明可用字段的简单语法

import scrapy


class DoubanMovieItem(scrapy.Item):
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()