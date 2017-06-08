from classes import Tree
from serialization import serialize_tree
from data_import import get_train

def build_trees(n, train, target, n_random_columns, max_depth):
    trees = []

    sample_size = int(round(len(train) / n))

    for i in range(0, n):
        trees.append(Tree(train.sample(sample_size), target, n_random_columns, max_depth))
    return trees


def build_bagging_trees(n, train, target, max_depth):
    # toma todas las columnas para hacer el split
    return build_trees(n, train, target, (len(train.columns) - 1), max_depth)


def main():

    train = get_train()
    trees = build_bagging_trees(25, train, 'duracion', 5, 20)
    i = 0
    for tree in trees:
        serialize_tree(tree, (str(i) + 'Florencia.pkl')) #poner cada uno su nombre
        i += 1

main()