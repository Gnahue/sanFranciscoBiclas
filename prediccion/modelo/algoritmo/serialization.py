import pickle

def serialize_tree(tree, file_name):
    output = open(file_name,'wb')
    pickle.dump(tree, output)
    output.close()

def desserialize_tree(file_name):
    pkl_file = open(file_name, 'rb')
    return pickle.load(pkl_file)

