import requests
from requests.exceptions import RequestException
import re
import time
import json


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return parse(response.text)
    return None


def parse(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    list = []
    for item in items:
        list.append({
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        })
    return list


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    data = []
    data.extend(get_page(url))
    write_data(data)


def write_data(data):
    with open('mao.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')


def page_nums(nums):
    for i in range(nums):
        main(offset=i*10)
        time.sleep(1)


page_nums(10)
