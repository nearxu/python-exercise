import urllib.request


def run_demo():
    response = urllib.request.urlopen('http://www.baidu.com')
    print(response.read().decode('utf-8'))
    print(type(response))
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))


if __name__ == '__main__':
    run_demo()
