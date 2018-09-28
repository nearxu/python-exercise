import scrapy
from scrapy.http import Request, FormRequest

class GithubSpider(scrapy.Spider):
    name='github'
    start_urls = [
        'https://github.com/issues',
    ]
    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "https://github.com/",
    }

    def start_requests(self):
        return [Request("https://github.com/login",
                        meta={'cookiejar': 1}, callback=self.post_login)]
    
    def post_login(self,response):
        authenticity_token = response.xpath(
            '//input[@name="authenticity_token"]/@value').extract_first()

        print(authenticity_token,'+++++++++auth++++++++')
        return [FormRequest.from_response(response,
                                          url='https://github.com/session',
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.post_headers,  # 注意此处的headers
                                          formdata={
                                              'utf8': '✓',
                                              'login': 'nearxu',
                                              'password': 'xsp3833858',
                                              'authenticity_token': authenticity_token
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

        
    def after_login(self,response):
        print(response.text,'+++++++++++response++++++++')
        # for url in self.start_urls:
        #     yield Request(url,meta={'cookiejar': response.meta['cookiejar']})

    # def parse_page(self,response):
    #     title =  response.xpath(
    #         '//span[@class="js-issue-title"]/text()').extract_first()
    #     print(title,'++++++++++title+++++++')