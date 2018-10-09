import pandas as pd

df = pd.DataFrame({'Country':['China','US','Japan','EU','UK/Australia', 'UK/Netherland'],
               'Number':[100, 150, 120, 90, 30, 2]})
# print(df)

a = df.drop('Country',axis=1).join(df['Country'].str.split('/',expand=True).stack().reset_index(level=1,drop=True).rename('Counter'))

print(a)

# 合并取平均数
b = a.groupby('Counter').mean()

# b= a.pivot_table('Counter',aggfunc = sum)
print(b)