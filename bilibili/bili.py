# -*- coding: utf-8 -*-

import requests
import json
import random
import sys
import time
import datetime


def datetime_to_timestamp_in_milliseconds(d):
    current_milli_time = lambda: int(round(time.time() * 1000))
    return current_milli_time()


head = {
    'User-Agent':
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
    'X-Requested-With':
    'XMLHttpRequest',
    'Referer':
    'http://space.bilibili.com/45388',
    'Origin':
    'http://space.bilibili.com',
    'Host':
    'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH':
    'AlexaToolbar/alx-4.0',
    'Accept-Language':
    'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept':
    'application/json, text/javascript, */*; q=0.01',
}

uas = [
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"
]

proxies = {
    'http': 'http://121.31.138.203:8123',
    'http': 'http://125.70.13.77:8080',
    'http': 'http://106.75.226.36:808',
    'http': 'http://61.135.217.7:80',
    'http': 'http://60.247.59.182:44671',
    'http': 'http://183.62.207.242:32755',
    'http': 'http://218.7.221.166:31485',
    'http': 'http://27.41.181.175:80',
    'http': 'http://218.76.253.201:61408',
    'http': 'http://175.155.24.28:808',
    'http': 'http://202.103.12.30:60850',
    'http': 'http://61.157.206.172:59656',
    'http': 'http://175.148.72.52:1133'
}

urls = []

for m in range(1600, 2000):
    for n in range(m * 100, (m + 1) * 100):
        url = 'http://space.bilibili.com/ajax/member/GetInfo?mid=' + str(n)
        urls.append(url)


def getsource(url):
    payload = {
        '_':
        datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
        'mid':
        url.replace('http://space.bilibili.com/ajax/member/GetInfo?mid=', '')
    }
    ua = random.choice(uas)
    head = {
        'User-Agent':
        ua,
        'Referer':
        'http://space.bilibili.com/' + str(random.randint(9000, 10000)) + '/'
    }

    jscontent = requests.session().post(
        'http://space.bilibili.com/ajax/member/GetInfo',
        headers=head,
        data=payload,
        proxies=proxies).text

    try:
        jsdict = json.loads(jscontent)
        statusjson = jsdict['status'] if 'status' in jsdict.keys() else False

        if statusjson == True:
            if 'data' in jsdict.keys():
                jsData = jsdict['data']
                mid = jsData['mid']
                name = jsData['name']
                sex = jsData['sex']
                level = jsData['level_info']['current_level']
                place = jsData['place'] if 'place' in jsData.keys() else 0
                print(mid, name)
            else:
                print('no data now')
        else:
            print('error' + url)
    except ValueError:
        print('decoding json has fail')


if __name__ == '__main__':
    for key in urls:
        getsource(key)
