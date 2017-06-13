import csv
from predictions import write_csv

def get_dict(file_name):
    d = {}
    print ('--------------> OBTENIENDO PREDICCION DE: '+ file_name)
    f = open(file_name, 'rb')
    f.next() # saltea id, duration
    reader = csv.reader(f)
    for row in reader:
        d[int(row[0])] = int(round(float(row[1])))

    f.close()

    return d

def get_avg(i_name, n):
    d = get_dict(str(0)+ i_name)

    for i in range(1, n):
        dict_i = get_dict(str(i)+ i_name)
        for key in d:
            d[key] += dict_i[key]

    for key in d:
        d[key] = (d[key]/ n)

    return d.items()

def get_avg_notebook(n):
    # codigo para notebook
    d = get_dict('../../modelo/algoritmo/' + str(0) + 'prediction.csv')

    for i in range(1, n):
        dict_i = get_dict('../../modelo/algoritmo/' + str(i) + 'prediction.csv')
        for key in d:
            print (dict_i[key])
            d[key] += dict_i[key]

    for key in d:
        d[key] = (d[key]/ n)

    return d.items()


def main():
    
    n = 1000
    # cantidad de predicciones que tenemos
    i_name = 'prediction.csv' 
    # nombre comun de los n csvs ej: 0prediction.csv, 1prediction.csv => prediction.csv
    
    avg = get_avg(i_name, n)
    # get_avg_dicts calcula el promedio de todos los csvs
    
    write_csv(avg, 'csvs_avg.csv')
    # y escribe el resultado en csvs_avg.csv


# main()