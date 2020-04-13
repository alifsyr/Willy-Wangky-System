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

            
            
user_data = loadfile(input('Masukan nama File User: ')) # user.csv
print(user_data)
wahana_data = loadfile(input('Masukan nama File Daftar Wahana: ')) # wahana.csv
pembelian_data = loadfile(input('Masukan nama File Pembelian Tiket: ')) # pembelian.csv
penggunaan_data = loadfile(input('Masukan nama File Penggunaan Tiket: ')) # penggunaan.csv
tiket_data = loadfile(input('Masukkan nama File Kepemilikan Tiket: ')) # tiket.csv
refund_data = loadfile(input('Masukkan nama File Refund Tiket: ')) # refund.csv
kritiksaran_data = loadfile(input('Masukkan nama File Kritik dan Saran: ')) #kritiksaran.csv

print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")