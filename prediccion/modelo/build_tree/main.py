from classes import Tree
import pandas as pd


def get_predictions(df_test, tree):
    results = []

    for i in range(0, len(df_test)):
        df_register = df_test.ix[i:i]
        # TODO: Ir guardandolo directamente en un csv
        # por ahora se guarda en results como: (id , prediccion)
        results.append((df_register.id.values[0], tree.get_prediction(df_register)))

    return results


def main():
    # (train,test) = data_import.data_import()

    # tree = Tree(train, 'duration', 4, 2)

    # results = get_predictions(test, tree)

    train = pd.read_csv('../../Data/youtube_train.csv')
    test = pd.read_csv('../../Data/youtube_test.csv')

    tree = Tree(train, 'hours', 2, 6)  # esto es para bagging

    results = get_predictions(test, tree)
    # tree.print_leafs()

    # prediction = tree.get_prediction(train.ix[5:5])
    print results



main()
