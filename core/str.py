#!/usr/bin/env python
# coding=utf-8

#字符串截取

a = 'hello world'
print(a[1:5])
print(a[:])  ##表示截取全部
print(a[3:])  #表示从a[3]开始，一直到字符串的最后'
print(a[:5])  #表示从字符串开头一直到a[4]前结束

#strip() 去掉字符串的左右空格 rstrip() lstrip() 去掉字符串的左边空格

# split
line = 'hello i am coding!'
listsa = line.split(' ')

print(listsa)

# join

name = ['welcome', 'to', 'new york']

print(''.join(name))