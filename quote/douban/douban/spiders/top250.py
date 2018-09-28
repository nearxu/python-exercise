# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem 
import re
class Top250Spider(CrawlSpider):
    name = 'top250'
    # allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor( restrict_xpaths='//div[@class="article"]/ol[@class="grid_view"]/li'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]/a[contains(., "后页")]'))
    )

    def __init__(self):
        self.headers = {
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',            
            'Accept-Encoding':'gzip, deflate',            
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = DoubanItem()
        num = response.xpath('//div[@class="top250"]/span[@class="top250-no"]/text()').extract()[0]
        item['ranking'] = int(re.sub(r'\D','',num))
        item['movie_name'] = response.xpath('//div[@id="content"]/h1/span/text()').extract()[0]
        item['score'] = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()[0]
        item['info'] = "".join(response.xpath('//div[@id="link-report"]/span/text()').extract())
        item['doctor'] = response.xpath('//span[@class="attrs"]/a/text()').extract()[0]
        actors = response.xpath('//span[@class="actor"]/span[@class="attrs"]/span/a/text()').extract()
        print(actors[0:3],'++++++++++++++actors++++++++')
        item['actor'] = actors[0:3]
        item['img'] = response.xpath('//div[@id="mainpic"]/a/img/@src').extract()[0]
        yield item


