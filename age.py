import pandas as pd
import datetime

date_list = [{'yyyy-mm-dd': '1973-10-15'},
         {'yyyy-mm-dd': '1970-12-25'},
         {'yyyy-mm-dd': '2003-11-15'}]
df = pd.DataFrame(date_list, columns = ['yyyy-mm-dd'])

def extract_year(row):
    return row.split('-')[0]

def extract_year1(year, current_year):
    return current_year - int(year)

def korean_year(year, current_year):  
    return current_year - int(year) + 1

df['year'] = df['yyyy-mm-dd'].apply(extract_year)
df['age'] = df['year'].apply(extract_year1, current_year=2022)
df['kage'] = df['year'].apply(korean_year, current_year=2022)
print(df)

now = datetime.datetime.now()
print(now.year)
