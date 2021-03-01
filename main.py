import pandas as pd
import csv

df = pd.read_csv('data.csv')

req_headers = ['Name', 'Distance', 'Mass', 'Radius', 'Constellation', 'Declination', 'App.mag.', 'Orbitalperiod', 'Semimajoraxis', 'Ecc.', 'Discovery year']
all_headers = list(df.columns.values)

for h in all_headers:
  if h not in req_headers:
    del df[h]
    
df.to_csv('final.csv', encoding="utf-8")
