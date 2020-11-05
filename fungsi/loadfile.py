import csv

def load(x):
    with open(x) as csvfile :
        reader = csv.reader (csvfile, delimiter=',')
        data = [row for row in reader]
    
    return data