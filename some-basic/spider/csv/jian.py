import csv
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.cnblogs.com/pick/#'

articles=[]
data_list = []

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

for i in range(2,7):
  url = base_url+'p{}'.format(i)
  print(url,'url')
  response = requests.get(url,headers=headers)
  print(response,'response')
  html = response.text
  print(type(html))
  soup = BeautifulSoup(html,'html.parser')

  for article in soup.find_all(class_='content'):
    title=article.find(class_='title').get_text()
    author = article.find(class_='blue-link').get_text()
    time = article.span['data-shared-at']
    articles.append([title,author,time])

with open('jianshu.csv','w') as f:
  writer = csv.writer(f)
  writer.writerow(['title','author','time'])
  for row in articles:
    writer.writerow(row)