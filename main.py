# Tugas Besar IF1210 Dasar Pemrograman
# Kelompok X

from fungsi import loadfile, login

'''
Zachrandika Alif Syahrzea
I Gede Govindabhakta
Ryandito Diandaru
'''

# KAMUS GLOBAL
'''
    user_data           : array of array of string
'''


command = str(input())

if command == "loadfile":
    user_data           = loadfile.loadfile(input('Masukan nama File User: ')) # user.csv
    wahana_data         = loadfile.loadfile(input('Masukan nama File Daftar Wahana: ')) # wahana.csv
    pembelian_data      = loadfile.loadfile(input('Masukan nama File Pembelian Tiket: ')) # pembelian.csv
    penggunaan_data     = loadfile.loadfile(input('Masukan nama File Penggunaan Tiket: ')) # penggunaan.csv
    tiket_data          = loadfile.loadfile(input('Masukkan nama File Kepemilikan Tiket: ')) # tiket.csv
    refund_data         = loadfile.loadfile(input('Masukkan nama File Refund Tiket: ')) # refund.csv
    kritiksaran_data    = loadfile.loadfile(input('Masukkan nama File Kritik dan Saran: ')) #kritiksaran.csv
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
    
#test
#print(user_data[1][0])