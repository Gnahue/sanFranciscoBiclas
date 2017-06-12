from classes import Tree
from serialization import serialize_tree
from data_import import get_train
import time
import datetime

def build_RF_trees(n, train, target, n_random_columns, max_depth, sample_size):

    for i in range(0, n):
        print ('CREANDO ARBOL ' + str(i) )
        ts = time.time()
        print (datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S'))
        tree = Tree(train.sample(sample_size), target, n_random_columns, max_depth)
        serialize_tree(tree, (str(i) + 'RF_5_5.pkl'))
        print ('<------------------------------------ARBOL NUEVO = ' + str(i) + ' ------------------------------------>')
        print ('SE CREO EN: ' +  str((time.time()-ts) / 60) + 'MINUTOS')


def build_bagging_trees(n, train, target, max_depth, sample_size):
    # toma todas las columnas para hacer el split =  bagging
    return build_RF_trees(n, train, target, (len(train.columns) - 1), max_depth, sample_size)


def main():

    train = get_train()

    n = 500 # cantidad de arboles a crear

    sample_size = int(round(len(train) / 4)) # sample with replacement

    max_depth = 5 # estudiar cual es la profundidad que funciona mejor

    # build_bagging_trees(n, train, 'duration', max_depth, 5000)
    build_RF_trees(n, train, 'duration', 5, max_depth, sample_size)


main()