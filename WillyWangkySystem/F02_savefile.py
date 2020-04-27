import csv


def save(data, names):
    import modules
    for i in range(modules.panjang(names)):     # Melakukan looping berdasarkan panjang array names
        name = str(input("Masukkan nama file " + str(names[i]) + " :"))     # input nama file csv
        writeFile(name, data[i])    # Memanggil fungsi writeFile
        
def writeFile(namaFile, arrayData):
    datafile = open(namaFile, "w", newline="")      # Membuka file dari hasil input name pada fungsi save dengan fungsi open dan menggunakan metode w untuk menulis 
    writer = csv.writer(datafile, delimiter=',')    
    for row in arrayData:
        writer.writerow(row)