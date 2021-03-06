import numpy as np
import csv

def get_tree_prediction(df_test, tree):
    prediction = {}
    for i in range(0, len(df_test)):
        df_register = df_test.ix[i:i]
        prediction[df_register.id.values[0]] = tree.get_prediction(df_register)
    return prediction


def get_trees_prediction(df_test, trees):
    
    if len(trees) == 1:
        return get_tree_prediction(df_test, trees[0]).items()  #[(k, value)]

    print ("Prediciendo en el arbol: 0")
    predictions_sum = get_tree_prediction(df_test, trees[0])

    # predictions_sum = {id1: prediction, id2: prediction}

    for i in range(1, len(trees)):
        print ("Prediciendo en el arbol: " + str(i))
        prediction = get_tree_prediction(df_test, trees[i])

        for key in prediction:
            predictions_sum[key] += prediction[key]
            # {id1: prediction + new_prediction, id2: prediction + new_prediction}

    print ("Calculo del promedio de resultados")

    for key in predictions_sum:
        predictions_sum[key] = round((predictions_sum[key] / len(trees)), 5)

    return predictions_sum.items()

def write_csv(results, file_name):

    print ("--------------> ESCRIBIENDO " + file_name)
    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([('id','duration')])
        writer.writerows(results)
