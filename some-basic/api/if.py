#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')