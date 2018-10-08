import pandas as pd

tips = pd.read_csv('tips.csv')
print(tips.head())

print(tips.index)

print(tips.columns)

print(tips.values)