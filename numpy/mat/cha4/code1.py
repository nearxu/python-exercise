import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
# from scipy.interpolate import lagrange

data = pd.read_excel('../data/catering_sale.xls')
data[(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None
df = data[data[u'销量'].notnull()]
# df = data[data[u'销量'].isnull()]
# index_list = df[u'销量'].index

# def play(index,df,k=5):
#     y = df[list(range(index-k,index))+list(range(index + 1, index + 1 + k))]
#     y = y[y.notnull()]
#     print(y,'++++++y')
#     return y
    # print(lagrange(y.index, list(y))(index))
    # return lagrange(y.index, list(y))(index)

# for index in index_list:
#     data[[u'销量']][index] = play(index,data[u'销量'])

# print(data)

print(df)
