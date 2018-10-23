import requests
from bs4 import BeautifulSoup

ss = requests.session()
ss.proxies = {
    'http': 'http://123.206.6.17:3128',
    'https': 'http://123.206.6.17:3128'
}
print(ss.get('http://www.qq.com'))