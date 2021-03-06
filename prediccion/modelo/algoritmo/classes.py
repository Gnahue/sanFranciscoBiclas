import random
import pandas as pd
import numpy as np

from split_std import *


class Leaf(object):
    def __init__(self, value):
        self.value = value
    def get_value(self):
        return self.value

    def comply_condition(self, df_register):
        return True

    def get_prediction(self, df_register):
        return self.value

    def get_leafs_values(self):
        return [self.value]


class Node(object):
    max_depth = 0

    def __init__(self, df, target, feature, value_condition, depth):
        self.target = target
        self.feature = feature
        self.value_condition = value_condition
        self.depth = depth
        self.nodes = self.build_nodes(df)

    def any_node_comply_condition(self, df_register):
        for node in self.nodes:
            if node.comply_condition(df_register):
                return node
        return None

    def get_leafs_values(self):
        leafs_values = []
        for node in self.nodes:
            leafs_values = leafs_values + node.get_leafs_values()
        return leafs_values

    def get_median_leafs(self):
        leafs_values = self.get_leafs_values()
        return round(np.median(np.array(leafs_values)))

    def comply_condition(self, df_register):
        return df_register[self.feature].values[0] == self.value_condition

    def get_prediction(self, df_register):
        node = self.any_node_comply_condition(df_register)
        if not node:
            # print('CORTO LA PREDICCION EN PROFUNDIDAD: ' + str(self.depth) )
            return self.get_median_leafs()
        else:
            return node.get_prediction(df_register)

    def create_node(self, df, feature, value_condition):
        # value_condition es la condicion del nodo
        # creo un nuevo df que tenga solo aquellos
        # registros que cumplan la condicion,

        df_partition = df.loc[df[feature] == value_condition]
        return (Node(df_partition, self.target, feature, value_condition, (self.depth + 1)))

    def build_nodes(self, df):
        # 1- definir cuantos nodos vamos a tener
        # de acuerdo a la cantidad de distintos valores
        # del feature

        # 2- dividir el data frame y colocarlo 
        # en el nodo que corresponda segun cada
        # valor del feature de este nodo

        if (len(df) == 1) or (self.depth == Node.max_depth):
            # en este caso el df tiene un solo registro
            # o llegamos a profundidad maxima
            # estamos ante una hoja

            nodes = [Leaf(df[self.target].mean())]
            return nodes

        nodes = []
        nodes_feature = get_split(df, self.target, 4)
        unique_values = df[nodes_feature].unique()

        for value_condition in unique_values:
            nodes.append(self.create_node(df, nodes_feature, value_condition))

        return nodes

class Root(object):
    def __init__(self, df, target, n_columns):
        self.target = target
        self.feature = get_split(df, target, n_columns)
        self.nodes = self.build_nodes(df)

    def create_node(self, df, value_condition):
        df_partition = df.loc[df[self.feature] == value_condition]

        if len(df_partition) == 1:
            return Leaf(df[self.target].mean())

        return Node(df_partition, self.target, self.feature, value_condition, 1)

    def build_nodes(self, df):

        nodes = []

        unique_values = df[self.feature].unique()

        for value_condition in unique_values:
            nodes.append(self.create_node(df, value_condition))

        return nodes

    def get_prediction(self, df_register):
        for node in self.nodes:
            if node.comply_condition(df_register):
                return node.get_prediction(df_register)


class Tree(object):
    def __init__(self, df, target, n_columns, max_depth):
        # target = nombre de la columna a predecir
        # n_columns =  cantidad de columnas random a considerar en cada split
        # n_columns < len(df.columns)!!!
        # para bagging n_columns = len(df.columns) - 1
        # es decir que termina tomando todas las columnas

        # seteamos la variable de clase max_depth
        Node.max_depth = max_depth
        self.root = Root(df, target, n_columns)

    def get_prediction(self, df_register):
        return self.root.get_prediction(df_register)

