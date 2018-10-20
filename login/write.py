#!/usr/bin/env python
# coding=utf-8
import json
import random
data = ['HTTPS://106.75.226.36808\n' 'HTTP://61.135.217.780\n']

# with open('./ip.text', 'w', encoding='utf-8') as fp:
#     fp.writelines(data)

with open('./ip.txt', 'r', encoding='utf-8') as files:
    filde = files.readlines()
    print(filde)
    print(type(filde))

    IP = random.choice(filde)
    print(IP)
