import pandas as pd
import os
import math

df = pd.read_csv(os.path.dirname(__file__) + '/tall-building-inventory-1.csv', engine='python') # test with , nrows=20
df['Latitude'] = 0.0
df['Longitude'] = 0.0
df['polygon'] = df['polygon'].astype(str)

o_rows = len(df.index)
i_float = 0
for index, row in df.iterrows():
    if not (row['polygon'] == '' or row['polygon'] == 'nan'):
        data = row['polygon'][10:-2].split(',')
        data = [x.strip() for x in data]
        coordinates = [x.split(' ') for x in data]
        coordinates = [[y.replace('(','').replace(')','') for y in x] for x in coordinates]
        coordinates = [[float(y) for y in x] for x in coordinates]
        df = df.append([row]*len(coordinates),ignore_index=True)        
    else:
        coordinates = [[None, None]]
        df = df.append([row]*len(coordinates),ignore_index=True)

    start = o_rows + i_float
    for i in range(start, start + len(coordinates)):
        df['Longitude'][i] = coordinates[i - start][0]
        df['Latitude'][i] = coordinates[i - start][1] 

    i_float += len(coordinates)

df = df.iloc[o_rows:]
df.reset_index(inplace=True)
print(df)
df.to_csv(os.path.dirname(__file__) + '/blueprint.csv', encoding='utf-8', index=False)