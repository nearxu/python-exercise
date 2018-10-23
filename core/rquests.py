import requests

url = 'http://upload-images.jianshu.io/upload_images/5831032-3e4d3f9ad5a61b78.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1080/q/50'

data = requests.get(url)

with open('request.jpg', 'wb') as fo:
    fo.write(data.content)