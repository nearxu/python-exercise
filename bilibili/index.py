# -*-coding:utf8-*-

import requests
import json
import random
import sys
import datetime
import time
from imp import reload


def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time():
        return int(round(time.time() * 1000))

    return current_milli_time()


reload(sys)


def userAgent(file):
    uas = []
    with open(file, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1 - 1])
    random.shuffle(uas)
    return uas


uas = userAgent("user_agent.txt")

head = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
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

proxies = {
    'http': 'http://120.26.110.59:8080',
    'http': 'http://120.52.32.46:80',
    'http': 'http://218.85.133.62:80',
}
time1 = time.time()

urls = []


def getsource(url):
    print(url, 'url')
    payload = {
        '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
        'mid': url.replace('https://space.bilibili.com/', '')
    }
    ua = random.choice(uas)
    head = {
        'User-Agent':
        ua,
        'Referer':
        'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(
            random.randint(10000, 50000))
    }
    jscontent = requests.session().post(
        'http://space.bilibili.com/ajax/member/GetInfo',
        headers=head,
        data=payload,
        proxies=proxies).text
    try:
        jsDict = json.loads(jscontent)

        statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
        if statusJson == True:
            print(jsDict)
            with open('near.json', 'w') as f:
                json.dump(jsDict, f)
        else:
            print('no data now')

    except Exception as e:
        print(e)
        pass


for m in range(5214, 5215):

    for i in range(m * 100, (m + 1) * 100):
        url = 'https://space.bilibili.com/' + str(i)
        print(url)
        getsource(url)
