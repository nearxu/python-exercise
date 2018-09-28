# -*- coding: utf-8 -*-

import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

data =pd.read_excel('data/catering_dish_profit.xls',index_col=u'菜品名')
data = data[u'盈利'].copy()

data.sort_values(ascending=False)

plt.figure()

data.plot(kind='bar')
plt.ylabel(u'盈利(元)')
p = 1.0 * data.cumsum() / data.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.ylabel(u'盈利（比例）')
plt.show()
