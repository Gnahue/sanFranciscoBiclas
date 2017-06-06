import dataImport 
import build_tree


def main():

	(train,test) = dataImport()

	build_tree(train, 'duration', n_columns, max_depth, min_size)
	