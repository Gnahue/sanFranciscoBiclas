import pandas as pd
import numpy as np

def dataImport():
    trip_train = pd.read_csv("../Data/trip_train.csv")
    trip_train.start_date = pd.to_datetime(trip_train.start_date, format='%m/%d/%Y %H:%M') 
    trip_train.end_date = pd.to_datetime(trip_train.end_date, format='%m/%d/%Y %H:%M')
    

    trip_test = pd.read_csv("../Data/trip_test.csv")
    trip_test.start_date = pd.to_datetime(trip_test.start_date, format='%m/%d/%Y %H:%M') 
    trip_test.end_date = pd.to_datetime(trip_test.end_date, format='%m/%d/%Y %H:%M')

    # weather = pd.read_csv("Data/weather.csv")      
    # station = pd.read_csv("Data/station.csv")
    # tanto weather como station son archivos que nos 
    # permiten usar para la prediccion, si es necesario
    # los usaremos

    # Dado a que para el algoritmo solo vamos a manejar variables numericas:
    # eliminamos la columna de start_station_name y dejamos start_station_id
    # eliminamos la columna de end_station_name y dejamos start_station_id
    trip_train.drop(['start_station_name','end_station_name'],inplace=True,axis=1)
    trip_test.drop(['start_station_name','end_station_name'],inplace=True,axis=1)



    # # en subscription_type tenemos dos posibles valores, subcriber o customer el primero sera 1 y el segundo 2
    trip_train["subscription_type"][trip_train["subscription_type"] == "Subscriber"] = 1
    trip_train["subscription_type"][trip_train["subscription_type"] == "Customer"] = 2
    trip_train["subscription_type"] = trip_train["subscription_type"].astype(int)
    trip_test["subscription_type"][trip_test["subscription_type"] == "Subscriber"] = 1
    trip_test["subscription_type"][trip_test["subscription_type"] == "Customer"] = 2
    trip_test["subscription_type"] = trip_test["subscription_type"].astype(int)


    # train["Age"] = train["Age"].fillna(train["Age"].median())  para valores faltantes

    return (trip_train,trip_test)


#(x,y) = dataImport()
#print x.head(20)

def dataImportNaiveBayes():
    (trip_train,trip_test) = dataImport()
    
    # Por ahora no se usan, los elimino
    trip_train.drop(['bike_id','zip_code'],inplace=True,axis=1)
    trip_test.drop(['bike_id','zip_code'],inplace=True,axis=1)
    
    trip_train['end_date_weekday'] = trip_train.end_date.dt.weekday
    trip_train['start_date_weekday'] = trip_train.start_date.dt.weekday
    trip_train['end_date_month'] = trip_train.end_date.dt.month
    trip_train['start_date_month'] = trip_train.start_date.dt.month
    trip_train['end_date_hour'] = trip_train.end_date.dt.hour
    trip_train['start_date_hour'] = trip_train.start_date.dt.hour
    
    trip_test['end_date_weekday'] = trip_test.end_date.dt.weekday
    trip_test['start_date_weekday'] = trip_test.start_date.dt.weekday
    trip_test['end_date_month'] = trip_test.end_date.dt.month
    trip_test['start_date_month'] = trip_test.start_date.dt.month
    trip_test['end_date_hour'] = trip_test.end_date.dt.hour
    trip_test['start_date_hour'] = trip_test.start_date.dt.hour
    
    
    trip_train['delta_duration'] = trip_train.duration - (trip_train.end_date - trip_train.start_date).dt.total_seconds()
    trip_train['delta_duration'] = trip_train['delta_duration'].apply(np.round).astype(int)
    
    trip_train.loc[(trip_train.start_date < '2013-11-03 02:00:00') & (trip_train.end_date > '2013-11-03 02:00:00'), ['delta_duration']] -= 3600
    trip_train.loc[(trip_train.start_date < '2014-11-02 02:00:00') & (trip_train.end_date > '2014-11-02 02:00:00'), ['delta_duration']] -= 3600
    trip_train.loc[(trip_train.start_date < '2014-03-09 03:00:00') & (trip_train.end_date > '2014-03-09 03:00:00'), ['delta_duration']] += 3600
    trip_train.loc[(trip_train.start_date < '2015-03-08 03:00:00') & (trip_train.end_date > '2015-03-08 03:00:00'), ['delta_duration']] += 3600
    
    trip_train = trip_train[(trip_train.delta_duration <= 60) & (trip_train.delta_duration >= -60)]

    return (trip_train,trip_test)