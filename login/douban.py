#!/usr/bin/env python
# encoding=utf-8

import requests
import re
from bs4 import BeautifulSoup
import codecs
from openpyxl import Workbook
wb = Workbook()
dest_filename = '电影.xlsx'
ws1 = wb.active
ws1.title = "电影top250"

base_url = 'http://movie.douban.com/top250/'


def download_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    print(data)
    print('*' * 20)
    return data


def parse(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    ol = soup.find('ol', class_='grid_view')
    name = []  # 名字
    star_con = []  # 评价人数
    score = []  # 评分
    info_list = []  # 短评

    for i in ol.find_all('li'):
        detail = i.find('div', attrs={'class': 'hd'})
        movie_name = detail.find(
            'span', attrs={
                'class': 'title'
            }).get_text()  # 电影名字
        level_star = i.find(
            'span', attrs={
                'class': 'rating_num'
            }).get_text()  # 评分
        star = i.find('div', attrs={'class': 'star'})
        star_num = star.find(text=re.compile('评价'))  # 评价

        info = i.find('span', attrs={'class': 'inq'})  # 短评

        if info:  # 判断是否有短评
            info_list.append(info.get_text())
        else:
            info_list.append('无')
        score.append(level_star)

        name.append(movie_name)
        star_con.append(star_num)

        # nextpage
        page = soup.find('span', attrs={'class': 'next'}).find('a')

        if page:
            return name, star_con, score, info_list, base_url + page['href']
        return name, star_con, score, info_list, None


def main():
    url = base_url
    name = []
    star_con = []
    score = []
    info = []
    while url:
        doc = download_page(url)
        movie, star, level_num, info_list, url = parse(doc)
        name = name + movie
        star_con = star_con + star
        score = score + level_num
        info = info + info_list
    for (i, m, o, p) in zip(name, star_con, score, info):
        col_A = 'A%s' % (name.index(i) + 1)
        col_B = 'B%s' % (name.index(i) + 1)
        col_C = 'C%s' % (name.index(i) + 1)
        col_D = 'D%s' % (name.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = m
        ws1[col_C] = o
        ws1[col_D] = p
    wb.save(filename=dest_filename)


if __name__ == '__main__':
    main()