from serialization import desserialize_tree
from predictions import get_trees_prediction
from predictions import write_csv
from data_import import get_test


def main():

    trees = [] #los 100 arboles creados

    for i in range(0, 20):
        trees.append(desserialize_tree(str(i)+'BaggingFlorencia.pkl'))

    # for i in range(0, 25):
    #     trees.append(desserialize_tree(str(i)+'Nahuel.pkl'))
    #
    # for i in range(0, 25):
    #     trees.append(desserialize_tree(str(i)+'Maximiliano.pkl'))
    #
    # for i in range(0, 25):
    #     trees.append(desserialize_tree(str(i)+'Pablo.pkl'))

    test = get_test()


    test = test.head(1)

    #definir la particion del test


    write_csv(get_trees_prediction(test, trees))

main()
