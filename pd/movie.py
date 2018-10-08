import pandas as pd

data = pd.read_csv('movie_metadata.csv')

# print(data)
# 添加默认值
data.country = data.country.fillna('None Given')

data.duration = data.duration.fillna(data.duration.mean())
# data = data[data['duration'] > 0]
sum_duration = data['duration'].sum()

avter_duration = sum_duration/len(data)

print(avter_duration) 

print(data.describe())

# 107.2

# 删除任何包含 NA 值的行
# data.dropna()

# 一行中至少要有 5 个非空值
# data.drop(thresh=5)

# 想要不知道电影上映时间的数据：
# data.dropna(subset=['title_year'])
# print(data.columns)


# 条件查询

# session_data = data[data['session'] = 1]

# drop_duplicates() 来删除重复数据

# data1 = data.drop_duplicates(['movie_title'],inplace=True)

# print(data1)

