import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

from pandas.core.series import Series

data = pd.read_csv('near.csv')
# labels ='男','女','非人类','null'

def city(adds):
    address = data[adds].value_counts()
    print(address)
    return address

def gender(type):
    genders = df[type].value_counts()
    return genders

def favorCount(type):
    favor = df[type].value_counts()
    print(favor)
    return favor

df = city('locations').sort_values(ascending=False)

print(df,'++++++df++++++')
plt.figure()

plt.plot(kind='bar')
plt.ylabel(u'city')
p = 1.0 * df.cumsum() / df.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.show()





