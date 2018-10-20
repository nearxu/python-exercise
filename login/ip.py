# -*- coding:UTF-8 -*-

from bs4 import BeautifulSoup
import subprocess as sp
from lxml import etree
import requests
import random
import re
import json


def get_proxy(page=1):
    sessiona = requests.Session()
    target_url = 'http://www.xicidaili.com/nn/%d' % page

    target_headers = {
        'Upgrade-Insecure-Requests':
        '1',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':
        'http://www.xicidaili.com/nn/',
        'Accept-Encoding':
        'gzip, deflate, sdch',
        'Accept-Language':
        'zh-CN,zh;q=0.8',
    }

    response = sessiona.get(url=target_url, headers=target_headers)
    response.encoding = 'utf-8'
    html = response.text

    ip_list = BeautifulSoup(html, 'lxml')
    ip_list1 = BeautifulSoup(str(ip_list.find_all(id='ip_list')), 'lxml')
    ip_list_info = ip_list1.table.contents

    proxy_list = []

    for index in range(len(ip_list_info)):
        if index % 2 == 1 and index != 1:
            dom = etree.HTML(str(ip_list_info[index]))
            ip = dom.xpath('//td[2]')
            port = dom.xpath('//td[3]')
            protocol = dom.xpath('//td[6]')
            proxy_list.append({'protocol': protocol, 'ip': ip, 'port': port})
    return proxy_list


def check_ip(ip, lose_time, waste_time):
    #命令 -n 要发送的回显请求数 -w 等待每次回复的超时时间(毫秒)
    cmd = "ping -n 3 -w 3 %s"
    #执行命令
    p = sp.Popen(
        cmd % ip, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    #获得返回结果并解码
    out = p.stdout.read().decode("gbk")
    #丢包数
    lose_time = lose_time.findall(out)
    #当匹配到丢失包信息失败,默认为三次请求全部丢包,丢包数lose赋值为3
    if len(lose_time) == 0:
        lose = 3
    else:
        lose = int(lose_time[0])
    #如果丢包数目大于2个,则认为连接超时,返回平均耗时1000ms
    if lose > 2:
        #返回False
        return 1000
    #如果丢包数目小于等于2个,获取平均耗时的时间
    else:
        #平均时间
        average = waste_time.findall(out)
        #当匹配耗时时间信息失败,默认三次请求严重超时,返回平均好使1000ms
        if len(average) == 0:
            return 1000
        else:
            #
            average_time = int(average[0])
            #返回平均耗时
            return average_time


def initpattern():
    #匹配丢包数
    lose_time = re.compile(u"丢失 = (\d+)", re.IGNORECASE)
    #匹配平均时间
    waste_time = re.compile(u"平均 = (\d+)ms", re.IGNORECASE)
    return lose_time, waste_time


def save_ip(lists):
    with open('./ip.txt', 'w', encoding='UTF-8') as fp:
        fp.writelines(lists)


ip_lists = []

if __name__ == '__main__':
    #初始化正则表达式
    lose_time, waste_time = initpattern()
    proxy_list = get_proxy()
    for proxy in proxy_list:
        ip = proxy['ip'][0].text
        average_time = check_ip(ip, lose_time, waste_time)
        if average_time > 200:
            proxy_list.remove(proxy)
            print('ip 链接超时，重新获取', ip)
        else:
            url = proxy['protocol'][0].text + '://' + proxy['ip'][
                0].text + ':' + proxy['port'][0].text + '\n'
            print(proxy['port'][0].text, 'ip')
            ip_lists.append(url)
    save_ip(ip_lists)
