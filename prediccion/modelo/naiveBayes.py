from __future__ import print_function
import pandas as pd
import numpy as np
import dataImport
import math

def naive_bayes():
    (train,test) = dataImport.dataImportNaiveBayes()
    
    clases = ('delta_duration', range(-59,61))
    stations_ids = [2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,23,
                    24,25,26,27,28,29,30,31,32,33,34,35,36,37,
                    38,41,42,45,46,47,48,49,50,51,39,54,55,56,
                    57,58,59,60,61,62,63,64,65,66,67,68,69,70,
                    71,72,73,74,75,76,77,80,82,83,84]
    variables_prediccion = [('start_station_id', stations_ids),
                            ('end_station_id', stations_ids),
                            ('start_date_weekday', range(7)),
                            ('start_date_hour', range(24)),
                            ('start_date_month', range(1,13)),
                            ('subscription_type', range(1,3))]
    
    modelo = crear_modelo(train, clases, variables_prediccion)
    dataframe_prediccion = predecir(test, modelo, clases, variables_prediccion)
    #print (modelo)
    return dataframe_prediccion

def crear_modelo(train, clases, variables_prediccion):
    modelo = {}
    for clase in clases[1]:
        print ('Delta duration --- ',clase)
        prob_clase = math.log10(len(train[ train[clases[0]] == clase ]) / float(len(train)))
        #prob_clase = 1 / float(120)
        modelo[clase] = (prob_clase, {})
        for variable in variables_prediccion:
            modelo[clase][1][variable[0]] = {}
            suma_de_frecuencias = 0
            for valor in variable[1]:
                # Se hace un recuento de valores y se aplica la correccion de laplace
                modelo[clase][1][variable[0]][valor] = len(train[ (train[clases[0]] == clase) & (train[variable[0]] == valor) ]) + 1
                suma_de_frecuencias += modelo[clase][1][variable[0]][valor]
            for valor in variable[1]:
                modelo[clase][1][variable[0]][valor] /= float(suma_de_frecuencias)
                modelo[clase][1][variable[0]][valor] = math.log10(modelo[clase][1][variable[0]][valor])
    return modelo

num_row = 0
intervalo = 1000

def predecir_row(row, modelo, clases, variables_prediccion, total_rows):
    prob_clase_dada_variables = 0
    mayor_prob = -100
    clase_mayor_prob = 0
    for clase in clases[1]:
        prob_clase = modelo[clase][0]
        prob_variables_dada_clase = 0
        for variable in variables_prediccion:
            prob_variables_dada_clase += modelo[clase][1][variable[0]][row[variable[0]]]
        prob_clase_dada_variables = prob_clase + prob_variables_dada_clase
        #print ('Prob ',clase,': ',prob_clase_dada_variables)
        if (prob_clase_dada_variables > mayor_prob):
            mayor_prob = prob_clase_dada_variables
            clase_mayor_prob = clase
    #print (clase_mayor_prob)
    global num_row
    global intervalo
    num_row += 1
    if (num_row >= intervalo):
        print (num_row,'/',total_rows)
        intervalo += 1000
    #print ('---------------')
    return clase_mayor_prob + np.round((row.end_date - row.start_date).total_seconds()).astype(int)

def predecir(test, modelo, clases, variables_prediccion):
    df = test
    total_rows = len(test)
    df ['duration'] = df.apply(predecir_row, axis=1, args=(modelo,clases,variables_prediccion, total_rows))
        
    df.loc[(df.start_date < '2013-11-03 02:00:00') & (df.end_date > '2013-11-03 02:00:00'), ['duration']] -= 3600
    df.loc[(df.start_date < '2014-11-02 02:00:00') & (df.end_date > '2014-11-02 02:00:00'), ['duration']] -= 3600
    df.loc[(df.start_date < '2014-03-09 03:00:00') & (df.end_date > '2014-03-09 03:00:00'), ['duration']] += 3600
    df.loc[(df.start_date < '2015-03-08 03:00:00') & (df.end_date > '2015-03-08 03:00:00'), ['duration']] += 3600
    return df

dataframe_prediccion = naive_bayes()
dataframe_prediccion.loc[:,['id','duration']].to_csv('naiveBayes.csv', index=False)