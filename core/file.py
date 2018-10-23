#!/usr/bin/env python
# coding=utf-8

with open('test.txt', 'w') as fp:
    for i in range(100):
        x = 1.0 / (i - 100)
        fp.write('hello world:' + str(i) + '\n')