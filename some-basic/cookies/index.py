
import requests
from bs4 import BeautifulSoup

url = 'http://www.imooc.com/u/2379448'
coo = 'imooc_uuid=8062f183-5579-4e63-bf43-528db6f24e61; imooc_isnew_ct=1492831625; PHPSESSID=oohki1kib5vfua4mhhr4aalmf6; loginstate=1; apsid=U5M2NlNWJmOGU4ODY5YjJlYTkxZjEwMzIzOTc5Y2UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjM3OTQ0OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGU2ZGJjYWVmMjVkYTNlYjRkMDIwM2ZiMzc4ZjM5NDY5CZ8EWQmfBFk%3DNj; IMCDNS=0; imooc_isnew=2; cvde=59049de1aa803-72'

cookies = {}

for content in coo.split(';'):
  name, value = content.split('=', 1)
  cookies[name] = value

headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

print(cookies)
r = requests.get(url, cookies,headers=headers)

print(r, 'response----------------------------')

html = r.text

soup = BeautifulSoup(html, 'html.parser')

print(soup)

print(r.headers)

# {'Server': 'nginx', 'Date': 'Mon, 06 May 2019 09:51:06 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Set-Cookie': 'imooc_uuid=92997c1e-a585-4ab1-a4e4-e459be05afa2; expires=Tue, 05-May-2020 09:51:06 GMT; Max-Age=31536000; path=/; domain=.imooc.com, imooc_isnew=1; expires=Tue, 05-May-2020 09:51:06 GMT; Max-Age=31536000; path=/; domain=.imooc.com, imooc_isnew_ct=1557136266; expires=Tue, 05-May-2020 09:51:06 GMT; Max-Age=31536000; path=/; domain=.imooc.com, cvde=5cd0038a5ff4e-1; path=/; domain=.imooc.com', 'Content-Encoding': 'gzip', 'X-Varnish': '329303167', 'Age': '0', 'Via': '1.1 varnish (Varnish/6.0)', 'X-Cache': 'MISS from CS42', 'Accept-Ranges': 'bytes'}
