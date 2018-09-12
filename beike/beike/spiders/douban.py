# -*- coding: utf-8 -*-

from scrapy import Request
from scrapy.spiders import Spider
from beike.items import BeikeItem


class MoiveSpider(Spider):
    name = 'moive'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        moives = response.xpath('//ol[@class="grid_view"]/li')
        for moive in moives:
            link = moive.xpath('.//div[@class="hd"]/a/@href').extract()[0]
            yield Request(link, headers=self.headers, callback=self.parse_detail)
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)

    def parse_detail(self, response):
        item = BeikeItem()
        moives = response.xpath('//div[@id="content"]')
        item['title'] = moives.xpath(
            '//h1/span/text()').extract()[0]
        item['ranking'] = moives.xpath(
            '//div[@class="top250"]/span[@class="top250-no"]/text()').extract()[0]
        item['name'] = moives.xpath(
            "//span[@class='attrs']/a/text()").extract()[0]
        # item['start'] = moives.xpath(
        #     '//div[@class="rating_self"]/strong[@class="rating_num"]').extract()[0]
        item['info'] = moives.xpath(
            "//div[@class='indent']/span[@class='short']/span/text()").extract()[0]
