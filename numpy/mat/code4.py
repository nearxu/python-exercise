import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel('data/catering_sale_all.xls', index_col=u'日期')

data.corr()
fz = data.corr()[u'百合酱蒸凤爪']
fzj = data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺'])

print(fz)

print('++++++++++++')

print(fzj)