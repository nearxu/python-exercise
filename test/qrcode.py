import requests

# r = requests.get("https://github.com/favicon.ico")
# print(r.text)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
