import requests
from urllib.parse import urlencode
import os
from hashlib import md5

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)

    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('响应成功')
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            # 不知道怎么处理没有的语法 ？？？？？
            if images:
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('url'), headers=headers)
        if response.status_code == 200:
            print('获取图片的响应成功')
            file_path = '{0}/{1}.{2}'.format(item.get('title'),
                                             md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    data = get_images(json)
    print(data, 'data')
    for item in data:
        print(item)
        save_image(item)


main(2)
