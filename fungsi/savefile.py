import csv
import modules

def save(data, names):
    for i in range(modules.panjang(names)):
        name = str(input("Masukkan nama file ", names[i], ":", sep=""))
        saveFile(name, data[i])
        
def saveFile(namaFile, arrayData):
    datafile = open(namaFile, "w")
    writer = csv.writer(datafile, delimiter=',')

    for row in arrayData:
        writer.writerow(row)