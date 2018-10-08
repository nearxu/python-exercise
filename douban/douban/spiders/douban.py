import scrapy
from douban.items import DoubanItem

class douabn_movies(scrapy.Spider):
    name='top250'
     # 如果网站设置有防爬措施，需要添加上请求头信息，不然会爬取不到任何数据
    headler = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '
                      'Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    # 开始链接
    start_urls = [
        'https://movie.douban.com/top250'
    ]
    
    def parse(self,response):
        print(response)
        item = DoubanItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').extract()[0]
            item["url"] = movie.xpath(
                './/div[@class="pic"]/a/@href').extract()[0],
            item["img"] = movie.xpath(
                './/div[@class="pic"]/a/img/@src').extract()[0],
            item["info"] = movie.xpath(
                './/div[@class="bd"]/p[@class="quote"]/span/text()').extract()[0]
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield scrapy.Request(next_url, headers=self.headers)