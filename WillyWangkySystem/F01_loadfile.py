import csv

def load():
    user_data           = loadfile(input('Masukkan nama File User: ')) # user.csv
    wahana_data         = loadfile(input('Masukkan nama File Daftar Wahana: ')) # wahana.csv
    pembelian_data      = loadfile(input('Masukkan nama File Pembelian Tiket: ')) # pembelian.csv
    penggunaan_data     = loadfile(input('Masukkan nama File Penggunaan Tiket: ')) # penggunaan.csv
    tiket_data          = loadfile(input('Masukkan nama File Kepemilikan Tiket: ')) # tiket.csv
    refund_data         = loadfile(input('Masukkan nama File Refund Tiket: ')) # refund.csv
    kritiksaran_data    = loadfile(input('Masukkan nama File Kritik dan Saran: ')) #kritiksaran.csv
    tikethilang_data    = loadfile(input('Masukkan nama File Tiket Hilang: ')) #lostticket.csv
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")

    return user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data

def autoLoad():
    user_data           = loadfile("data/user.csv") # user.csv
    wahana_data         = loadfile("data/wahana.csv") # wahana.csv
    pembelian_data      = loadfile("data/pembelian.csv") # pembelian.csv
    penggunaan_data     = loadfile("data/penggunaan.csv") # penggunaan.csv
    tiket_data          = loadfile("data/tiket.csv") # tiket.csv
    refund_data         = loadfile("data/refund.csv") # refund.csv
    kritiksaran_data    = loadfile("data/kritiksaran.csv") #kritiksaran.csv
    tikethilang_data    = loadfile("data/lostticket.csv") #lostticket.csv
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load secara autohmahtis bruh.")

    return user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data


def loadfile(x):
    with open(x) as csvfile :
        reader = csv.reader (csvfile, delimiter=',')
        data = [row for row in reader]
    
    return data

