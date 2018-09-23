import requests
from requests.auth import HTTPBasicAuth

r = requests.get('url',
                 auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)
