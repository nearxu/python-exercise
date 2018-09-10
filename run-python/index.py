# coding:utf-8
import requests
import os
import time
from lxml import html

# 图片链接列表，标题
# url是详情页链接


def getPage(pageNum):
    baseUrl = 'http://www.mzitu.com/page/{}'.format(pageNum)
    selector = html.fromstring(requests.get(baseUrl).content)
    urls = []
    for i in selector.xpath('//ul[@id="pins"]/li/a/@href'):
        urls.append(i)
    return urls


def getPiclink(url):
    sel = html.fromstring(requests.get(url).content)
    # 图片总数
    total = sel.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0]
    # 标题
    title = sel.xpath('//h2[@class="main-title"]/text()')[0]
    jpList = []
    for i in range(int(total)):
        link = '{}/{}'.format(url, i+1)
        s = html.fromstring(requests.get(link).content)
        jpg = s.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        jpList.append(jpg)
    return title, jpList


def downloadPic((title, piclist)):
    k = 1
    count = len(piclist)
    dirName = u'[%sp]%s' % (str(count), title)
    os.mkdir(dirName)

    for i in piclist:
        filename = '%s%s%s.jpg' % (os.path.abspath('.'), dirName, k)
        print u'开始下载图片:%s %s张 %(dirName,k)'

        with open(filename, "wb") as jpg:
            jpg.write(requests.get(i).content)
            time.sleep(0.5)
        k += 1


if __name__ == '__main__':
    #pageNum = input(u'请输入页码：')
    for link in getPage(2):
        downloadPic(getPiclink(link))
