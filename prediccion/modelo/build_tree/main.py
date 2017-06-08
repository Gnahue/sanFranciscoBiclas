from serialization import *
from data_import import data_import
from build_predictions import get_tree_prediction



def main():

    (train, test) = data_import()
    print get_tree_prediction(test, desserialize_tree('tree.pkl'))



main()
