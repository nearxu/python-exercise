#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from http import cookiejar


# class ZhihuSpider(scrapy.Spider):
#     name='zhihuLogin'
#     allowed_domains = ["www.zhihu.com"]
#     start_urls = [
#         "http://www.zhihu.com"
#     ]

#     headers = {"Accept": "*/*",
#         "Accept-Encoding": "gzip,deflate",
#         "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
#         "Connection": "keep-alive",
#         "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
#         "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
#         "Referer": "http://www.zhihu.com/"
#     }
#     def start_requests(self):
#         return [Request("https://www.zhihu.com/signup?next=%2F", meta = {'cookiejar' : 1}, callback = self.post_login)]
    
#     def post_login(self,response):
#         xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
#         print(xsrf,'++++++++xsrf++++++')
#         return [FormRequest.from_response(response,   #"http://www.zhihu.com/login",
#                             meta = {'cookiejar' : response.meta['cookiejar']},
#                             headers = self.headers,  #注意此处的headers
#                             formdata = {
#                             '_xsrf': xsrf,
#                             'email': '2448895924@qq.com',
#                             'password': 'xsp3833858'
#                             },
#                             callback = self.after_login,
#                             dont_filter = True
#                             )]
#     def after_login(self,response):
#         print(response.text,'+++++++++response+++++++++')
