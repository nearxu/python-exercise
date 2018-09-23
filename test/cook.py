import requests
# r = requests.get('https://www.baidu.com')
# print(r.cookies)

# for key, value in r.cookies.items():
#     print('key: '+key+'value: '+value)

# response = requests.get('https://www.12306.cn')
# print(response.status_code)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
