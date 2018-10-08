import pandas as pd
import numpy as np

data = pd.read_excel('catering_sale.xls',index_col=[u'日期'])
# data = pd.read_csv('catering_sale.xls')

print(data)