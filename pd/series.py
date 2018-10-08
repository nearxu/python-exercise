import numpy as np
import pandas as pd

data = [1,2,3]
index = ['a','b','c']

s= pd.Series(data=data,index=index,name='sss')
print(s)

print(s.index)

print(s.values)


data1=[
    [1,2,3],
    [4,5,6]
]

index1 = ['a','b']
col = ['A','B','C']

df = pd.DataFrame(data=data1,index=index1,columns=col)

print(df)


data3 = { 'A' : { 'a':1, 'b':4}, 'B': {'a':2,'b':5}, 'C':{'a':3, 'c':6} }
df1 = pd.DataFrame(data=data3)
print(df1)