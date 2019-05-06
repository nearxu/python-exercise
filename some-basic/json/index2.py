import urllib.request
import requests
import json

url = 'http://www.zimuzu.tv/public/hotkeyword'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

response = requests.get(url, headers=headers)

print(response, 'response')

html = response.content.decode('utf-8')

print(html, 'html')

# all this just for scrapy
# dicts = json.loads(html)

# print(dicts, 'dicts')
# arr = []

# for i in range(0, 10):
#     k = dicts['data'][i]['keyword']
#     arr.append(k)

# print(arr)