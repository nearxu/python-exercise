# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv('near.csv')

print('total count: ',len(data))

sortrd_data = data.sort_values(by='follower_count',ascending=False)

# print ('sort_fllower_data :',sortrd_data)

all_follower = sortrd_data['follower_count'].sum()

# print('all_foller',all_follower)

#gender

# male = data[]



