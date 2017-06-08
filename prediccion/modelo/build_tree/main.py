from classes import Tree
import pandas as pd


def get_predictions(df_test, tree):
    results = []

    # controlamos el csv test y esta bien indexado,
    # por eso podemos hacer esto:
    for i in range(0, len(df_test)):
        df_register = df_test.ix[i:i]
        # TODO: Ir guardandolo directamente en un csv
        # por ahora se guarda en results como: (id , prediccion)
        results.append((df_register.id.unique()[0], tree.get_prediction(df_register)))
    return results


def main():
    # (train,test) = dataImport.dataImport()

    # tree = build_tree.build_tree(train, 'duration', 4, 2)

    # results = get_predictions(test, tree)

    train = pd.read_csv('../../Data/youtube.csv')

    tree = Tree(train, 'hours', 4, 3)  # esto es para bagging

    tree.print_leafs()


main()
