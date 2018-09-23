from lxml import etree

html = etree.parse('./xp.html', etree.HTMLParser())
result = html.xpath('//ul/li/a/text()')
print(result)
