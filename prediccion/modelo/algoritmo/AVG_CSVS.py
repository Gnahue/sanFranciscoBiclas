import csv
from predictions import write_csv

def get_dict(file_name):
    d = {}

    f = open(file_name, 'rb')
    reader = csv.reader(f)
    for row in reader:
        d[float(row[0])] = float(row[1])

    f.close()

    return d

def get_avg(dicts):
    d = dicts[0]

    for i in range(1, len(dicts)):
        for key in d:
            d[key] += dicts[i][key]

    for key in d:
        d[key] = d[key]/ len(dicts)

    return d.items()

def main():
    dicts = []

    # get_dict crea dicts para cada results csv
    # Ej: results0.csv, results1.csv, results2.csv
    for i in range (0,3):
        dict_i = get_dict('results' + str(i) + '.csv')
        dicts.append(dict_i)

    # get_avg_dicts calcula el promedio de todos los csvs
    # y escribe el resultado en results.csv
    write_csv(get_avg(dicts))

main()