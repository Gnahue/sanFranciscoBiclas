import pandas as pd
import numpy as np

df = pd.read_csv("Data/trip_train.csv")
df.start_date = pd.to_datetime(df.start_date, format='%m/%d/%Y %H:%M') 
df.end_date = pd.to_datetime(df.end_date, format='%m/%d/%Y %H:%M')

#df['dura_min'] = (df.end_date - df.start_date).dt.seconds - 60
#df['dura_max'] = df.dura_min + 120
df['delta_duration'] = df.duration - (df.end_date - df.start_date).dt.total_seconds()

print ("-----------")
print (df.loc[:,['id','delta_duration']])
#print (len(df.duration.unique()))
print (len(df))
print (len(df[(df.delta_duration <= 60) & (df.delta_duration >= -60)]))
print (len(df[df.delta_duration > 60]))
print (len(df[df.delta_duration < -60]))

print ("-----------")

print (df[df.delta_duration > 60].loc[:,['id','duration','start_date','end_date','delta_duration']])
#print (df.info())