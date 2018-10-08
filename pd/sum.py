# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv('near.csv')

print('total count: ',len(data))

sortrd_data = data.sort_values(by='follower_count',ascending=False)

# print ('sort_fllower_data :',sortrd_data)

all_follower = sortrd_data['follower_count'].sum()

# print('all_foller',all_follower)

#gender

# data.gender = data.gender.fillna(data.gender.mean())
# data = data[data['gender'] >= 0]
# print(len(data))


male = len(data[data['gender'] == 0])
female = len(data[data['gender'] ==1])

print(male,female)

# 717 1361

# location
data.drop('locations', axis=1).join(data['locations'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('locations'))
#new_location = data['locations'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)
location = pd.value_counts(data['locations'])
items = []

for (k,v) in location.iteritems():
    items.append({
        'name': k if len(k) <= 2 else k[0:2],
        'count': v
    })
print(items)








