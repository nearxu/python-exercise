
import pandas as pd
import numpy as np

s =pd.Series()

print(s)
# Series([], dtype: float64)

data = np.array(['a','b','c','d'])

s1 = pd.Series(data)
s2 = pd.Series(data,index=[100,101,102,103])

print(s1)

print(s2)

data1 = {'a' : 0., 'b' : 1., 'c' : 2.}
s3 = pd.Series(data1)
print(s3)