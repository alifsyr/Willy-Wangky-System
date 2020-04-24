import csv


def save(data, names):
    import modules
    for i in range(modules.panjang(names)):
        name = str(input("Masukkan nama file ", names[i], ":", sep=""))
        writeFile(name, data[i])
        
def writeFile(namaFile, arrayData):
    datafile = open(namaFile, "w")
    writer = csv.writer(datafile, delimiter=',')

    for row in arrayData:
        writer.writerow(row)