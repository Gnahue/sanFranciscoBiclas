from classes import Tree

def get_tree_prediction(df_test, tree):
    prediction = []

    # for i in range(0, len(df_test)):
    for i in range(0, 10):
        df_register = df_test.ix[i:i]
        print df_register.head()

        # por ahora se guarda en results como: (id , prediccion)
        prediction.append((df_register.id.values[0], tree.get_prediction(df_register)))

    return prediction


def get_trees_prediction(df_test, trees):
    predictions = []
    # lista de las predicciones de todos los arboles
    # ex:  [[(id1,32),(id2,45)], [(id1,23),(id2,35)]]

    for tree in trees:
        predictions.append(get_tree_prediction(df_test, tree))

    # TODO:
    # calcular el promedio de las predicciones y retornar el csv

def build_trees(n, train, target, n_random_columns, max_depth):
    trees = []
    for i in range(0, n):
        trees.append(Tree(train, target, n_random_columns, max_depth))
    return trees


def build_bagging_trees(n, train, target, max_depth):
    # toma todas las columnas para hacer el split
    return build_trees(n, train, target, (len(train.columns) - 1), max_depth)

