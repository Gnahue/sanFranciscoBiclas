from classes import Tree
from serialization import serialize_tree
# from data_import import get_train
from data_import import data_import
import pandas as pd

def build_trees(n, train, target, n_random_columns, max_depth, sample_size):
    trees = []

    for i in range(0, n):
        trees.append(Tree(train.sample(sample_size), target, n_random_columns, max_depth))
        print ('<------------------------------------ARBOL NUEVO = ' + str(i) + ' ------------------------------------>')
    return trees


def build_bagging_trees(n, train, target, max_depth, sample_size):
    # toma todas las columnas para hacer el split
    return build_trees(n, train, target, (len(train.columns) - 1), max_depth, sample_size)


def main():

    # train = get_train()

    (train,test) = data_import()

    train.drop(['id', 'bike_id', 'mean_temperature_f', 'precipitation_inches'], inplace=True, axis=1)

    n = 100 # cantidad de arboles a crear

    sample_size = int(round(len(train) / n)) # sample with replacement

    max_depth = 25 # estudiar cual es la profundidad que funciona mejor

    trees = build_bagging_trees(n, train, 'duration', max_depth, 500)

    for tree in trees:
        print 'va'
        tree.print_leafs()

    # i = 0
    # for tree in trees:
    #     serialize_tree(tree, (str(i) + 'BaggingFlorencia.pkl')) #poner cada uno su nombre
    #     i += 1
    #
    # n_random_columns = int(round(len(train.columns) / 3))
    # # For regression a good default is: n_random_columns = features / 3
    # trees = build_trees(n, train, 'duration', n_random_columns, max_depth, sample_size)
    #
    # i = 0
    # for tree in trees:
    #     serialize_tree(tree, (str(i) + 'RFFlorencia.pkl')) #poner cada uno su nombre
    #     i += 1


main()