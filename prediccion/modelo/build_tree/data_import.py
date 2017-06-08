import pandas as pd
import numpy as np
import os.path

def data_import():


    # train["Age"] = train["Age"].fillna(train["Age"].median())  para valores faltantes


    file_train = "../Data/train.csv"
    file_test = "../Data/test.csv"
    exist_file_train = os.path.isfile(file_train)
    exist_file_test = os.path.isfile(file_test)


    if (not exist_file_train) or (not exist_file_test):
        weather = pd.read_csv("../Data/weather.csv")
        weather = transform_data_weather(weather)
        station = pd.read_csv("../Data/station.csv")
        station = transform_data_station(station)


    if not exist_file_train:
        trip_train = pd.read_csv("../Data/trip_train.csv")
        trip_train = transform_data_trip(trip_train, station, weather)
        trip_train.to_csv(file_train, index=False)
    else:
        trip_train = pd.read_csv(file_train)
    
    if not exist_file_test:
        trip_test = pd.read_csv("../Data/trip_test.csv")
        trip_test = transform_data_trip(trip_test, station, weather)
        trip_test.to_csv(file_test, index=False)
    else:
        trip_test = pd.read_csv(file_test)

    return (trip_train,trip_test)


def transform_data_trip(trip, station, weather):
    trip.start_date = pd.to_datetime(trip.start_date, format='%m/%d/%Y %H:%M') 

    trip["subscription_type"][trip["subscription_type"] == "Subscriber"] = 1
    trip["subscription_type"][trip["subscription_type"] == "Customer"] = 2
    trip["subscription_type"] = trip["subscription_type"].astype(int)

    trip['start_date_weekday'] = trip.start_date.dt.weekday
    trip['start_date_month'] = trip.start_date.dt.month
    trip['start_date_hour'] = trip.start_date.dt.hour

    # Son auxiliares para poder hacer el merge
    trip['start_date_year'] = trip.start_date.dt.year
    trip['start_date_day'] = trip.start_date.dt.day

    trip.drop(['start_station_name','end_station_name','end_date',
        'end_station_id','zip_code','start_date'],inplace=True,axis=1)
    #print len(trip)
    trip = pd.merge(trip, station, how='inner', left_on='start_station_id', right_on='id')
    #trip.drop(['id'], inplace=True, axis=1)
    #print len(trip)
    trip = pd.merge(trip, weather, how='left',left_on=['city','start_date_year','start_date_month',
        'start_date_day'], right_on=['city','year','month','day'])
    trip.drop(['start_date_year','start_date_day','year','month','day'], inplace=True, axis=1)
    #print len(trip)
    return trip

def transform_data_station(station):
    station.drop(['name','lat','long','dock_count','installation_date'],inplace=True,axis=1)
    return station

def transform_data_weather(weather):
    weather.date = pd.to_datetime(weather.date)
    weather.precipitation_inches = pd.to_numeric(weather.precipitation_inches, errors='coerce')
    weather.events.replace(to_replace=np.nan, value=0, inplace=True)
    weather.events.replace(to_replace='Fog', value=1, inplace=True)
    weather.events.replace(to_replace='Fog-Rain', value=2, inplace=True)
    weather.events.replace(to_replace='Rain', value=3, inplace=True)
    weather.events.replace(to_replace='rain', value=3, inplace=True)
    weather.events.replace(to_replace='Rain-Thunderstorm', value=4, inplace=True)
    weather.drop(['max_gust_speed_mph'],inplace=True,axis=1)
    #weather.dropna(inplace=True)

    # Son auxiliares para poder hacer el merge con trip
    weather['year'] = weather.date.dt.year
    weather['month'] = weather.date.dt.month
    weather['day'] = weather.date.dt.day

    # Se crea un dataframe auxiliar para agregarle la ciudad a weather,
    # para en un siguiente paso poder hacer join entre weather y trip
    city_zip_codes = pd.DataFrame(data=[
        ['San Francisco',94107],['San Jose',95113],['Redwood City',94063],
        ['Mountain View',94041],['Palo Alto',94301]], columns=['city', 'zip_code'])

    weather = pd.merge(weather, city_zip_codes, how='inner', on='zip_code')
    weather.drop(['zip_code','date'],inplace=True,axis=1)

    return weather