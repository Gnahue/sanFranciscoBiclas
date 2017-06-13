
from serialization import desserialize_tree
from predictions import get_tree_prediction
from predictions import get_trees_prediction
from predictions import write_csv
from data_import import get_test


def main():

    test = get_test()

    for i in range(0, 500):

    	tree = desserialize_tree(str(i)+'RF_5_5.pkl')  #ahi pongan el nombre de los arboles
    	write_csv(get_tree_prediction(test, tree).items(), str(i) + 'prediction.csv')  #aca va el nombre de como se crean los csv de resultados


    # for i in range(0, 25):
    #     trees.append(desserialize_tree(str(i)+'RFNahuel.pkl'))

main()
