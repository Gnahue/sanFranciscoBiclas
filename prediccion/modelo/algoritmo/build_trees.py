from classes import Tree
from serialization import serialize_tree
from data_import import get_train
from predictions import get_tree_prediction
from predictions import write_csv
import time
import datetime
from data_import import get_test


def build_RF_trees(n, train, target, n_random_columns, max_depth, sample_size):
    for i in range(0, n):
        print ('CREANDO ARBOL ' + str(i))
        print (datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S'))
        tree = Tree(train.sample(sample_size), target, n_random_columns, max_depth)
        serialize_tree(tree, (str(i) + 'RF_3_5.pkl'))
        print ('<------------------------------------ARBOL NUEVO = ' + str(i) + ' ------------------------------------>')
        print ('SE CREO EN: ' +  str((time.time()-ts) / 60) + ' MINUTOS')


def build_RF_trees_prediction(n, train, target, n_random_columns, max_depth, sample_size):

    test = get_test()
    for i in range(0, n):
    	print('________________________________________________________')
        print ('--------------> CREANDO ARBOL ' + str(i) +'...')
        ts = time.time()
    	print ('--------------> INICIO: ' + str(datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')))
        tree = Tree(train.sample(sample_size), target, n_random_columns, max_depth)
        print ('--------------> ARBOL NUEVO: ' + str(i))
        ts1 = time.time()
        print ('--------------> SE CREO EN: ' + str(round((ts1 - ts) / 60,2)) + ' MINUTOS ')
        print ('--------------> CALCULANDO PREDICCION...')
        write_csv(get_tree_prediction(test, tree).items(), str(i) + 'prediction.csv')  # aca va el nombre de como se crean los csv de resultados
        print ('--------------> SE CALCULO PREDICCION EN: ' + str(round((time.time() - ts1) / 60,2)) + ' MINUTOS')
        print ('--------------> DEMORO UN TOTAL DE: ' + str(round((time.time() - ts) / 60,2)) + ' MINUTOS')


def build_bagging_trees(n, train, target, max_depth, sample_size):
    # toma todas las columnas para hacer el split =  bagging
    return build_RF_trees(n, train, target, (len(train.columns) - 1), max_depth, sample_size)


def main():

    n = 500 # cantidad de arboles a crear

    train = get_train()

    n_random_columns = 3

    max_depth = 5 # estudiar cual es la profundidad que funciona mejor
    
    sample_size = int(round(len(train) / 4)) # sample with replacement


    # build_bagging_trees(n, train, 'duration', max_depth, 5000)
    build_RF_trees_prediction(n, train, 'duration', n_random_columns, max_depth, sample_size)


main()
