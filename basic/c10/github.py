#!/usr/bin/env python
# coding=utf-8

from requests import Session
from lxml import etree
from bs4 import BeautifulSoup


class LoginGithub(object):
    def __init__(self, username="****", password="*****"):
        self.username = username
        self.password = password
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.profile_url = 'https://github.com/settings/profile'
        # session维持会话, 不用cookies
        self.session = Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Referer': 'https://github.com',
        }

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token_value = selector.xpath(
            '//div[@id="login"]/form/input[2]/@value')[0]
        print(token_value)
        return token_value

    def login(self):
        post_data = {
            'authenticity_token': self.token(),
            'commit': 'Sign in',
            'login': self.username,
            'password': self.password,
            'utf8': '✓',
        }
        response = self.session.post(
            self.post_url,
            data=post_data,
            headers=self.headers
        )
        if response.status_code == 200:
            print('登录成功')
            self.parse_html(response.text)
        response = self.session.get(self.profile_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def parse_html(self, html):
        select = etree.HTML(html)
        # obj = BeautifulSoup(html, 'html.parser')
        # # //*[@id="dashboard"]/div[2]/div[7]
        # dynamics = select.xpath(
        #     '//*[@id="dashboard"]/div[2]/div[contains(@class, "watch_started")]')
        # div = obj.find('div', {'id': 'dashboard'})
        # print(div)
        # l2_div = div.find('div', {'class': 'news'})
        # print(l2_div)
        # divs = l2_div.find_all('div', {'class': 'watch_started'})
        # print(divs)
        # dashboard > div.news.column.two-thirds > div:nth-child(7)
        if dynamics:
            for dynamic in dynamics:
                """只看started, 还有follow 类的"""
                user = dynamic.xpath(
                    './/div[contains(@class, "width-full")]/div[contains(@class, "flex-items-baseline")]/div/a[1]/text()').strip()
                started_item = dynamic.xpath(
                    './/div[contains(@class, "width-full")]/div[contains(@class, "flex-items-baseline")]/div/a[2]/text()').strip()
                print('{} started {}'.format(user, started_item))

    def profile(self, html):
        selector = etree.HTML(html)
        user_profile_email = selector.xpath(
            '//select[@id="user_profile_email"]/option[last()]/text()')
        print('Your email is {}'.format(user_profile_email))


if __name__ == '__main__':
    ul = LoginGithub()
    ul.login()
