import urllib.request
from bs4 import BeautifulSoup
import os

url = 'http://www.yidianzixun.com/channel/u241'

response = urllib.request.urlopen(url)

print(type(response))
print(response,'response')

html = response.read().decode('utf-8')

soup = BeautifulSoup(html,'html.parser')

result = soup.find_all('img',limit=10)

print(result,'result')
links = []

for content in result:
  links.append(content.get('src'))

print(type(links))
print(links)