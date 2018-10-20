# -*-coding:utf8-*-

import requests
import json
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Referer':
    'http://music.163.com',
    'Host':
    'music.163.com'
}


def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print('request err')


def parse_info(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('ul', class_='f-hide').find_all('a')
    song_ids = []
    song_names = []
    for link in links:
        song_id = link.get('href').split('=')[-1]
        song_name = link.get_text()
        song_ids.append(song_id)
        song_names.append(song_name)
    return zip(song_names, song_ids)


def get_geci(song_id):
    url = 'http://music.163.com/api/song/lyric' + 'id=' + str(song_id)
    html = get_html(url)
    init_lyric = json_obj['lrc']['lyric']
    regex = re.compile(r'\[.*\]')
    final_lyric = re.sub(regex, '', init_lyric).strip()
    print(final_lyric)
    return final_lyric


if __name__ == '__main__':
    singer_id = input('请输入歌手id')
    start_url = 'http://music.163.com/artist?id={}'.format(singer_id)
    html = get_html(start_url)
    single_infos = parse_info(html)
    for single_info in single_infos:
        lyric = get_geci(single_info[1])
