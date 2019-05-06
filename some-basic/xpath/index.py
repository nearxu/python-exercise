from lxml import etree

html = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""


def getxpath(html):
    return etree.HTML(html)


h1 = getxpath(html)

a = h1.xpath('//title/text()')

b = h1.xpath('//h2/a/@src')

print(a)

print(b)
