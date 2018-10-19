import os
import json
import requests
from urllib.parse import urlencode
from multiprocessing import Pool
from multiprocessing import Pool
from hashlib import md5

BASE_URL = 'http://www.toutiao.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# 分线程爬取
GROUP_START = 1
GROUP_END = 10


def get_page(offset):
    print(offset)
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }

    url = BASE_URL + 'search_content/?' + urlencode(params)
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 200:
            return json.loads(resp.text)
    except requests.ConnectionError as e:
        print('Error: {}'.format(e.args))
        return None


def get_image(json):
    if json:
        for item in json:
            title = item.get('title')
            return title

# def save_img():
#     with open('./gril.json', 'w', encoding='utf-8') as fp:
#         for url in lists:
#             fp.write(url+"\n")


def save_img(item):
    if not os.path.exists(item.get('media_name')):
        os.mkdir(item.get('media_name'))
        try:
            if 'media_url' in item:
                response = requests.get(item.get('media_url'))
                if response.status_code == 200:
                    file_path = '{0}/{1}.{2}'.format(item.get('title'),
                                                     md5(response.content).hexdigest(), 'jpg')
                    if not os.path.exists(file_path):
                        with open(file_path, 'w') as fp:
                            fp.write(response.content)
                    else:
                        print('image is exisit')
            else:
                print('media_url is not exisit')
        except requests.ConnectionError as e:
            print(e)


def main(offset):
    json = get_page(offset)
    for item in json['data']:
        if item:
            save_img(item)


if __name__ == '__main__':
    pool = Pool()
    groups = [x*20 for x in range(GROUP_START, GROUP_END)]
    pool.map(main, groups)
    pool.close()
    pool.join()
