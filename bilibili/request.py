import requests

# r = requests.get('https://cuiqingcai.com')

# verify
r = requests.get('https://github.com', verify=True)
print(r.text)
print(r.status_code, 'code')
print(r.encoding, 'encoding')
