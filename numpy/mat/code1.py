
# -*- coding: utf-8 -*-

import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

IO = 'data/catering_sale.xls'

sheet = pd.read_excel(IO,index_col=u'日期')
# print(sheet)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()

p = sheet.boxplot(return_type='dict')
x= p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()
plt.show()
