import pandas as pd
import numpy as np
import os.path

def dataImport():
    file_train = "../Data/train.csv"
    file_test = "../Data/test.csv"


    if (not os.path.isfile(file_train)) or (not os.path.isfile(file_test)):
        #weather = pd.read_csv("../Data/weather.csv")
        station = pd.read_csv("../Data/station.csv")
        station = transform_data_station(station)


    if not os.path.isfile(file_train):
        trip_train = pd.read_csv("../Data/trip_train.csv")
        trip_train = transform_data_trip(trip_train, station)
        trip_train.to_csv(file_train, index=False)
    else:
        trip_train = pd.read_csv(file_train)
    
    if not os.path.isfile(file_test):
        trip_test = pd.read_csv("../Data/trip_test.csv")
        trip_test = transform_data_trip(trip_test, station)
        trip_test.to_csv(file_test, index=False)
    else:
        trip_test = pd.read_csv(file_test)

    # weather = pd.read_csv("Data/weather.csv")      
    # station = pd.read_csv("Data/station.csv")
    # tanto weather como station son archivos que nos 
    # permiten usar para la prediccion, si es necesario
    # los usaremos

    return (trip_train,trip_test)


def transform_data_trip(trip, station):
    trip.start_date = pd.to_datetime(trip.start_date, format='%m/%d/%Y %H:%M') 

    trip["subscription_type"][trip["subscription_type"] == "Subscriber"] = 1
    trip["subscription_type"][trip["subscription_type"] == "Customer"] = 2
    trip["subscription_type"] = trip["subscription_type"].astype(int)

    trip['start_date_weekday'] = trip.start_date.dt.weekday
    trip['start_date_month'] = trip.start_date.dt.month
    trip['start_date_hour'] = trip.start_date.dt.hour

    trip.drop(['start_station_name','end_station_name','id','start_date',
        'end_date','end_station_id','zip_code'],inplace=True,axis=1)

    trip = pd.merge(trip, station, how='inner', left_on='start_station_id', right_on='id')
    trip.drop(['id'], inplace=True, axis=1)

    return trip

def transform_data_station(station):
    station.drop(['name','lat','long','dock_count','installation_date'],inplace=True,axis=1)
    return station