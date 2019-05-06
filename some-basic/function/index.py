import time

def area(x, y=3.14):
    a = y * x * x
    print('area', a)
    return a


a = area(10)

# asctime
### some api from
#### https://www.yiibai.com/python3/python_date_time.html
localtime = time.asctime(time.localtime(time.time()))

print(localtime)