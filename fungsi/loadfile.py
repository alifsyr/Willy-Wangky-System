import csv

def loadfile(x):
    with open(x) as csvfile :
        reader = csv.reader (csvfile, delimiter=',')
        rownum = 0
        data = []

        for row in reader:
            data.append (row)
            rownum += 1
    
    return data