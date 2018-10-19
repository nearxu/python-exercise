import requests
from urllib.parse import urlencode
import json
# from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host':
    'm.weibo.cn',
    'Referer':
    'https://m.weibo.cn/u/2830678474',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest',
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)
    except requests.ConnectionError as e:
        print('error', e.args)


def get_parse(json):
    if json:
        for item in enumerate(json):
            item = item['mblog']
            weibo = {}
            weibo['id'] = item['id']
            # weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item['attitudes_count']
            weibo['comments'] = item['comments_count']
            weibo['reposts'] = item['reposts_count']
            return weibo


def save_data(data):
    if data:
        with open('near.json', 'w') as f:
            json.dump(data, f)


max_page = 5

if __name__ == '__main__':
    for page in range(1, max_page + 1):
        objects = get_page(page)
        # print(objects, 'objects')
        data = get_parse(objects['data'])
        print(data, 'data')
