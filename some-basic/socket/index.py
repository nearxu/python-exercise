import socket
import time

url = 'https://www.baidu.com/'
host = 'www.baidu.com'
port = 443
host_port = (host, port)

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(host_port)
s.sendall(b'CONNECT url:port/HTTP/1.1')

server_replay = s.recv(1000000)

# str与bytes之间的转换
print(type(server_replay))

print(str(server_replay,encoding='utf-8'))

print(bytes.decode(server_replay))
