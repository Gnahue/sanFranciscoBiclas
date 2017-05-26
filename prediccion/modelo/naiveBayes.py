import pandas as pd
import numpy as np
import dataImport

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
                            ('end_date_weekday', range(7)),
                            ('end_date_hour', range(24)),
                            ('end_date_month', range(1,13)),
                            ('subscription_type', range(1,3))]
    
    modelo = crear_modelo(train, clases, variables_prediccion)
    
    print (train.info())
    print (test.info())
    
    print modelo

def crear_modelo(train, clases, variables_prediccion):
    modelo = {}
    for clase in clases[1]:
        modelo[clase] = {}
        for variable in variables_prediccion:
            modelo[clase][variable[0]] = {}
            suma_de_frecuencias = 0
            for valor in variable[1]:
                # Se hace un recuento de valores y se aplica la correccion de laplace
                modelo[clase][variable[0]][valor] = len(train[ (train[clases[0]] == clase) & (train[variable[0]] == valor) ]) + 1
                suma_de_frecuencias += modelo[clase][variable[0]][valor]
            for valor in variable[1]:
                modelo[clase][variable[0]][valor] /= float(suma_de_frecuencias)
    return modelo

naive_bayes()