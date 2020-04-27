import csv

def load():
    user_data           = loadfile(input('Masukkan nama File User: '))              # user memberikan input nama file user.csv
    wahana_data         = loadfile(input('Masukkan nama File Daftar Wahana: '))     # user memberikan input nama file wahana.csv
    pembelian_data      = loadfile(input('Masukkan nama File Pembelian Tiket: '))   # user memberikan input nama file pembelian.csv
    penggunaan_data     = loadfile(input('Masukkan nama File Penggunaan Tiket: '))  # user memberikan input nama file penggunaan.csv
    tiket_data          = loadfile(input('Masukkan nama File Kepemilikan Tiket: ')) # user memberikan input nama file tiket.csv
    refund_data         = loadfile(input('Masukkan nama File Refund Tiket: '))      # user memberikan input nama file refund.csv
    kritiksaran_data    = loadfile(input('Masukkan nama File Kritik dan Saran: '))  # user memberikan input nama file kritiksaran.csv
    tikethilang_data    = loadfile(input('Masukkan nama File Tiket Hilang: '))      # user memberikan input nama file lostticket.csv
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")        

    return user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data

def autoLoad():
    user_data           = loadfile("data/user.csv")         # user memberikan input nama file user.csv
    wahana_data         = loadfile("data/wahana.csv")       # user memberikan input nama file wahana.csv
    pembelian_data      = loadfile("data/pembelian.csv")    # user memberikan input nama file pembelian.csv
    penggunaan_data     = loadfile("data/penggunaan.csv")   # user memberikan input nama file penggunaan.csv
    tiket_data          = loadfile("data/tiket.csv")        # user memberikan input nama file tiket.csv
    refund_data         = loadfile("data/refund.csv")       # user memberikan input nama file refund.csv
    kritiksaran_data    = loadfile("data/kritiksaran.csv")  # user memberikan input nama filekritiksaran.csv
    tikethilang_data    = loadfile("data/lostticket.csv")   # user memberikan input nama file lostticket.csv
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load secara automatis.")

    return user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data


def loadfile(x):
    with open(x) as csvfile :
        reader = csv.reader (csvfile, delimiter=',')
        data = [row for row in reader]
    
    return data

