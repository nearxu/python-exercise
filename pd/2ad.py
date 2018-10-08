import numpy as np
import pandas as pd

data =[1,2,3]
index = ['a','b','c']

s= pd.Series(data=data,index=index)

# print(s)


# print(s[1])

# 切片
# print(s[0:2])


# print(s[[0,2]])

#改

s1 = s.copy()
s1['a'] = 10

print(s1)

# s1.replace(to_replace = 10, value = 100, inplace=False)
# print(s1)

a = s1.drop(['a','c'])

print(a)


data1 = [[1,2,3],
        [4,5,6]]
index1 = ['a','b']
columns = ['A','B','C']
df = pd.DataFrame(data=data1, index=index1, columns = columns)

print(df)

print(df['A'])

print(df[['A','C']])

print(df[0:1])


df1 = df.copy()

df1.loc['a','A'] = 100

print(df1)

df2 = df1.replace(to_replace=100,value=10000,inplace=False)

print(df2)

df3 = pd.DataFrame([[22,33,44],[55,66,77]], index = ['c','d'],columns = ['A','B','C'])

df4 = pd.concat([df,df3],axis=0)

print(df4)

#  axis  0 行  1 列
df5 = df4.drop(['a'],axis=0)

print(df5)

del df5['A']
print(df5)