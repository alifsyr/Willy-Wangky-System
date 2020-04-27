import csv


def save(data, names):
    import modules
    folderDirectory = "data/"
    for i in range(modules.panjang(names)):     # Melakukan looping berdasarkan panjang array names
        name = str(folderDirectory + input("Masukkan nama file " + str(names[i]) + " :"))     # input nama file csv
        writeFile(name, data[i])    # Memanggil fungsi writeFile
    print('Data berhasil disimpan!')
    
def writeFile(namaFile, arrayData):
    
    with open(namaFile, mode='w',newline='') as csvfile:      # Membuka file dari hasil input name pada fungsi save dengan fungsi open dan menggunakan metode w untuk menulis 
        writer = csv.writer(csvfile)
        for row in arrayData:
            writer.writerow(row)