import pandas as pd
import numpy as np
import matplotlib as plt


df = pd.read_csv("Data/trip_test.csv")
df.start_date = pd.to_datetime(df.start_date, format='%m/%d/%Y %H:%M') 
df.end_date = pd.to_datetime(df.end_date, format='%m/%d/%Y %H:%M')

df['duration'] = (df.end_date - df.start_date).dt.total_seconds()
df['duration'] = df['duration'].apply(np.round).astype(int)

# Suma o resta una hora si hubo cambio horario
df.loc[(df.start_date < '2013-11-03 02:00:00') & (df.end_date > '2013-11-03 02:00:00'), ['duration']] -= 3600
df.loc[(df.start_date < '2014-11-02 02:00:00') & (df.end_date > '2014-11-02 02:00:00'), ['duration']] -= 3600
df.loc[(df.start_date < '2014-03-09 03:00:00') & (df.end_date > '2014-03-09 03:00:00'), ['duration']] += 3600
df.loc[(df.start_date < '2015-03-08 03:00:00') & (df.end_date > '2015-03-08 03:00:00'), ['duration']] += 3600

print ("-----------")
print (df.loc[:,['id','duration']])
df.loc[:,['id','duration']].to_csv('resta.csv', index=False)