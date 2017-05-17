import pandas as pd

def dataImport():
	trip_train = pd.read_csv("../Data/trip_train.csv")
	trip_train.start_date = pd.to_datetime(trip_train.start_date, format='%m/%d/%Y %H:%M') 
	trip_train.end_date = pd.to_datetime(trip_train.end_date, format='%m/%d/%Y %H:%M')

	trip_test = pd.read_csv("../Data/trip_test.csv")

	# weather = pd.read_csv("Data/weather.csv")  	
	# station = pd.read_csv("Data/station.csv")
	# tanto weather como station son archivos que nos 
	# permiten usar para la prediccion, si es necesario
	# los usaremos

	# Dado a que para el algoritmo solo vamos a manejar variables numericas:
	# eliminamos la columna de start_station_name y dejamos start_station_id
	# eliminamos la columna de end_station_name y dejamos start_station_id
	trip_train.drop(['start_station_name','end_station_name'],inplace=True,axis=1)



	# # en subscription_type tenemos dos posibles valores, subcriber o customer el primero sera 1 y el segundo 2
	trip_train["subscription_type"][trip_train["subscription_type"] == "Subscriber"] = 1
	trip_train["subscription_type"][trip_train["subscription_type"] == "Customer"] = 2


	# train["Age"] = train["Age"].fillna(train["Age"].median())  para valores faltantes

	return (trip_train,trip_test)


(x,y) = dataImport()
print x.head(20)



#df['dura_min'] = (df.end_date - df.start_date).dt.seconds - 60
#df['dura_max'] = df.dura_min + 120
# trip_train['delta_duration'] = trip_train.duration - (trip_train.end_date - trip_train.start_date).dt.total_seconds()

# print ("-----------")
# print (trip_train.loc[:,['id','delta_duration']])
# #print (len(df.duration.unique()))
# # Total de viajes
# print (len(df))
# # Duracion de viajes dentro del rango esperado
# print (len(df[(df.delta_duration <= 60) & (df.delta_duration >= -60)]))
# # Duracion de viajes que caen fuera del rango esperado
# print (len(df[df.delta_duration > 60]))
# print (len(df[df.delta_duration < -60]))

# ''' El delta_duration para los viajes que caen fuera del rango es de 
# 3600 segundos (1 hora) aprox.
# Segun pude ver en internet en esas fechas justo hubo un cambio de horario,
# se adelanto o se atrazo una hora.
# https://www.timeanddate.com/time/change/usa/san-francisco?year=2014
# '''

# print ("-----------")

# print (df[df.delta_duration > 60].loc[:,['id','duration','start_date','end_date','delta_duration']])
# #print (df.info())