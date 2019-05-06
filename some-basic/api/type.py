#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
# number int float complex

# str
s = 'python-中文'

print(s)

b = s.encode('utf-8')

print(b)

print(b.decode('utf-8'))

## asic ord and chr
print(ord('a'))

print(chr(98))

# list 有序的集合
classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)
print(classmates[0])

print(len(classmates))

# tuple 一旦初始化就不能修改
tuples = ['Michael', 'Bob', 'Tracy']

print(tuples[-1])

#dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

#time

localtime = time.localtime(time.time())

print(localtime)

### asctime()

asc = time.asctime(time.localtime(time.time()))

print(asc)