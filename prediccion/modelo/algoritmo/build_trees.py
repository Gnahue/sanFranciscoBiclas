from classes import Tree
from serialization import serialize_tree
from data_import import get_train

def build_RF_trees(n, train, target, n_random_columns, max_depth, sample_size):

    for i in range(0, n):
        print ('CREANDO ARBOL ' + str(i) )
        tree = Tree(train.sample(sample_size), target, n_random_columns, max_depth)
        serialize_tree(tree, (str(i) + 'RFFlorencia.pkl'))
        print ('<------------------------------------ARBOL NUEVO = ' + str(i) + ' ------------------------------------>')


def build_bagging_trees(n, train, target, max_depth, sample_size):
    # toma todas las columnas para hacer el split
    return build_RF_trees(n, train, target, (len(train.columns) - 1), max_depth, sample_size)


def main():

    train = get_train()

    n = 25 # cantidad de arboles a crear

    sample_size = int(round(len(train) / 4)) # sample with replacement

    max_depth = 20 # estudiar cual es la profundidad que funciona mejor

    #build_bagging_trees(n, train, 'duration', max_depth, 5000)
    build_RF_trees(n, train, 'duration', 3, max_depth, sample_size)



main()