import pandas as pd

df = pd.read_csv('../data/Artworks.csv').head(100)

df['Date'].value_counts()

row_with_dashes = df['Date'].str.contains('-').fillna(False)

for i, dash in df[row_with_dashes].iterrows():

    df.at[i,'Date'] = dash['Date'][0:4]

df['Date'].value_counts()


row_with_cs = df['Date'].str.contains('c').fillna(False)

for i,row in df[row_with_cs].iterrows():

    df.at[i,'Date'] = row['Date'][-4:]

df['Date'].value_counts()


df['Date'] = df['Date'].replace('Unknown','0',regex=True)

df['Date'] = df['Date'].replace('n.d.','0',regex=True)

df['Date'].value_counts()