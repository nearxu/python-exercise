import urllib.request
import json
import requests

# api from https://www.runoob.com/python/python-json.html

# json.dumps object => json

# json.loads json => dict

# demo1

url = 'http://www.weather.com.cn/data/cityinfo/101050101.html'

response = requests.get(url)

html = response.content.decode('utf-8')

print(html, 'html')

print(type(html))
# dic = json.dumps(html)
# print(dic, 'dic')

# str = json.dumps(html, ensure_ascii=False)

def write_weather(string):
  with open('wea.txt','w+',encoding='utf-8') as fp:
    fp.write(string)

write_weather(str)

# fp = open('wea.txt', 'w+', encoding='utf-8')

# fp.write(html)

# fp.close()