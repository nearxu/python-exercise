
import numpy as np
import pandas as pd

df1 = pd.DataFrame([[1,2],[3,4]], index = ['a','b'],columns = ['A','B'])
df2 = pd.DataFrame([[1,3],[4,8]], index = ['b','d'],columns = ['B','C'])

df3 = pd.merge(left = df1, right = df2, how = 'inner' ,left_index = True, right_index = True)

print(df3)

print(pd.concat([df1,df2],join='inner',axis=1))