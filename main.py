# Tugas Besar IF1210 Dasar Pemrograman
# Kelompok X

from fungsi import loadfile, login, signup, filterrides, ridehistory

'''
Zachrandika Alif Syahrzea
I Gede Govindabhakta
Ryandito Diandaru
Nabila Farras Ammara Mumtaz
'''

# KAMUS GLOBAL
'''
    user_data           : array of array of string
'''
endprogram              = False

while (not endprogram):
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
        
    if command =="loadfiletest":
        user_data           = loadfile.loadfile(input('Masukkan nama File user: '))

    if command == "signup":
        user_data = signup.signup(user_data)    
        
    if command == "riwayat":
        ridehistory.rideHistory(penggunaan_data)
        
    if command == "cari":
        filterrides.filterRides(wahana_data)
        
    if command == "exit":
        endprogram = True

#test
print(user_data)
