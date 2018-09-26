# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem 

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

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = DoubanItem()
        item['ranking'] = response.xpath('//div[@class="top250"]/span[@class="top250-no"]/text()').extract()[0]
        item['movie_name'] = response.xpath('//div[@id="content"]/h1/span/text()').extract()[0]
        item['score'] = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()[0]
        item['info'] = "".join(response.xpath('//div[@id="link-report"]/span/text()').extract())
        yield item


