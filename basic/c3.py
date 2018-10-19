#!/usr/bin/env python
# coding=utf-8

import json
import time
import requests
import re
from lxml import etree

base_url = 'http://maoyan.com/board/4'

Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}


def get_page(url, offset=1):
    if offset != 1:
        url += ('?offset='+str((offset-1)*10))
    data = requests.get(url, headers=Headers)
    if data.status_code == 200:
        return data.text
        # return etree.parse(data.text, etree.HTMLParser)
    # try:
    #     data = requests.get(url, headers=Headers)
    #     if data.status_code == 200:
    #         return data.text
    #     return None
    # except RequestException as e:
    #     return None


def parse_page(html):
    items = html.xpath('//div[@class="list-wrap"]/div[@class="item"]')
    print(items, 'items')
    for item in items:
        yield {
            '电影名': item.xpath('//div[@class="title"]/text()'),
        }


if __name__ == '__main__':

    for page in range(1, 2):
        html = get_page(base_url, page)
        items = parse_page(html)
        print(items)
        # for item in items:
        #     with open('./index.txt', 'a') as fp:
        #         fp.write(json.dumps(item, ensure_ascii=False)+'\n')
