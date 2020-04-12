import csv

def loadfile(x):
    if x == "user.csv":
        with open(x) as user :
            user_data = csv.reader (user, delimiter=',')
            for row in user_data:
                print(row)
    elif x == "wahana.csv":
        with open(x) as wahana :
            wahana_data = csv.reader (wahana, delimiter=',')
            for row in wahana_data:
                print(row)
    elif x == "tiket.csv":
        with open(x) as tiket :
            tiket_data= csv.reader (tiket, delimiter=',')
            for row in tiket_data:
                print(row)
    elif x == "refund.csv":
        with open(x) as refund :
            refund_data= csv.reader (refund, delimiter=',')
            for row in refund_data:
                print(row)            
    elif x == "penggunaan.csv":
        with open(x) as penggunaan :
            penggunaan_data= csv.reader (penggunaan, delimiter=',')
            for row in penggunaan_data:
                print(row)
    elif x == "pembelian.csv":
        with open(x) as pembelian :
            pembelian_data= csv.reader (pembelian, delimiter=',')
            for row in pembelian_data:
                print(row)
    else :
        with open(x) as kritiksaran :
            kritiksaran_data= csv.reader (kritiksaran, delimiter=',')
            for row in kritiksaran_data:
                print(row)
loadfile(input('Masukan nama File User: ')) # user.csv
loadfile(input('Masukan nama File Daftar Wahana: ')) # wahana.csv
loadfile(input('Masukan nama File Pembelian Tiket: ')) # pembelian.csv
loadfile(input('Masukan nama File Penggunaan Tiket: ')) # penggunaan.csv
loadfile(input('Masukkan nama File Kepemilikan Tiket: ')) # tiket.csv
loadfile(input('Masukkan nama File Refund Tiket: ')) # refund.csv
loadfile(input('Masukkan nama File Kritik dan Saran: ')) #kritiksaran.csv

print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")