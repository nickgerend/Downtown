# Written by: Nick Gerend, @dataoutsider
# Viz: "Downtown", enjoy!

import pandas as pd
import os
import math

df_blueprint = pd.read_csv(os.path.dirname(__file__) + '/building.csv', engine='python')
df_blueprint['index'] = df_blueprint['row'] - 1

df_info = pd.read_csv(os.path.dirname(__file__) + '/tall-building-inventory-1.csv', engine='python')
df_info = df_info.groupby('Date').agg({'Stories_Above_Grade':'mean', 'OBJECTID':'count'}).dropna().reset_index()
df_info['index'] = df_info['Date'] - df_info['Date'].min()

df_final = pd.merge(df_blueprint, df_info, on=['index'], how='left')
#df_final.index.rename('idx', inplace=False)
df_final.reset_index(inplace = True)
print(df_final)

df_final.to_csv(os.path.dirname(__file__) + '/blueprint_info.csv', encoding='utf-8', index=False)