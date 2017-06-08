from classes import *
import numpy as np


def std_value(df,column_name,value,target):
    # Retorna el valor del desvio standar de una columna contra la de target
    std = np.std(df.loc[df[column_name]==value,target].values.flatten())
    len = df[column_name].count()
    len_value = df.loc[df[column_name]==value,target].count()
    prob = float(len_value)/len
    return std*prob

def calculate_std(df,column_name,target):
    # calcula los valores de desvio standar para cada columna
    stds = 0
    unique_values = df[column_name].unique()
    for value in unique_values:
        stds +=  std_value(df,column_name,value,target)
    return stds

def calculate_stds(df,columns_name,target):
    stds=[]
    for column_name in columns_name:
        stds.append((column_name,calculate_std(df,column_name,target)))
    return stds
        
def final_stds(stds_columns,target_std):
    stds=[]
    for tupple in stds_columns:
        stds.append((tupple[0],target_std - tupple[1]))
    return stds

def get_nrandom_columns(df,target,n_columns):
    columns_name = df.columns.tolist()
    columns_name.remove(target)
    return [ columns_name[i] for i in sorted(random.sample(range(len(columns_name)), n_columns)) ]

def get_split(df,target,n_columns):
    # Calculo std de la variable a predecir
    target_std = np.std(df.ix[:, target].tolist())
    
    columns_name = get_nrandom_columns(df,target,n_columns)
    
    # Calculamos la desviacion standard de cada columna:
    # Esto es: la sumatoria de (la probabilidad de cada uno de los distintos valores
    # de una columna * la desviacion standar del mismo) 
    stds_columns = calculate_stds(df,columns_name,target)
    
    # Restamos cada std de columna al std del target
    stds_columns = final_stds(stds_columns,target_std)

    # Obtengo el maximo valor
    max_std_column_name = max(stds_columns,key=lambda item:item[1])[0]
    
    # Devolvemos el nombre de la columna con mayor diferencia de std
    return max_std_column_name

