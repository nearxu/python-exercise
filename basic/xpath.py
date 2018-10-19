

#!/usr/bin/env python
# coding=utf-8


# Python中利用xpath解析HTML
# https://zhuanlan.zhihu.com/p/29436838
# 多个属性匹配
#xpath('//li[contains(@class, "li") and @name="item"]/a/text()')


import codecs
from lxml import etree

html = etree.parse('./a.html', etree.HTMLParser())
result = html.xpath('//ul/li/a/text()')
print(result)
