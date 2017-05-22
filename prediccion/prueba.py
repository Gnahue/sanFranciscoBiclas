import pandas as pd
import numpy as np
import matplotlib as plt


df = pd.read_csv("Data/trip_train.csv")
df.start_date = pd.to_datetime(df.start_date, format='%m/%d/%Y %H:%M') 
df.end_date = pd.to_datetime(df.end_date, format='%m/%d/%Y %H:%M')

#print (df[df.start_date == '2014-11-01 17:05:00'].loc[:,['id','duration','start_date','end_date']])
#print (df.sort_values('start_date').loc[:,['id','duration','start_date','end_date']])
df['delta_duration'] = df.duration - (df.end_date - df.start_date).dt.total_seconds()
df['delta_duration'] = df['delta_duration'].apply(np.round).astype(int)

df.loc[(df.start_date < '2013-11-03 02:00:00') & (df.end_date > '2013-11-03 02:00:00'), ['delta_duration']] -= 3600
df.loc[(df.start_date < '2014-11-02 02:00:00') & (df.end_date > '2014-11-02 02:00:00'), ['delta_duration']] -= 3600
df.loc[(df.start_date < '2014-03-09 03:00:00') & (df.end_date > '2014-03-09 03:00:00'), ['delta_duration']] += 3600
df.loc[(df.start_date < '2015-03-08 03:00:00') & (df.end_date > '2015-03-08 03:00:00'), ['delta_duration']] += 3600

print ("-----------")
print (df.loc[:,['id','delta_duration']])

#print (len(df.duration.unique()))
# Total de viajes
print (len(df))
# Duracion de viajes dentro del rango esperado
print (len(df[(df.delta_duration <= 60) & (df.delta_duration >= -60)]))
# Duracion de viajes que caen fuera del rango esperado
print (len(df[df.delta_duration > 60]))
print (len(df[df.delta_duration < -60]))


''' El delta_duration para los viajes que caen fuera del rango es de 
3600 segundos (1 hora) aprox.
Segun pude ver en internet en esas fechas justo hubo un cambio de horario,
se adelanto o se atrazo una hora.
https://www.timeanddate.com/time/change/usa/san-francisco?year=2014
'''


print ("-----------")

print (df[df.delta_duration > 60].loc[:,['id','duration','start_date','end_date','delta_duration']])
print ("-----------")
print (df[df.delta_duration < -60].loc[:,['id','duration','start_date','end_date','delta_duration']])
#print (df.info())

df[(df.delta_duration <= 60) & (df.delta_duration >= -60)].groupby('delta_duration').size().plot()