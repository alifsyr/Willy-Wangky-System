# Tugas Besar IF1210 Dasar Pemrograman
# Kelompok X

from fungsi import loadfile, login, signup

'''
Zachrandika Alif Syahrzea
I Gede Govindabhakta
Ryandito Diandaru
'''

# KAMUS GLOBAL
'''
    user_data           : array of array of string
'''
endprogram              = False

while (not endprogram):
    command = str(input("$ "))

    currentUser = ["", "", "", "", "", "notLoggedIn", ""]

    if command == "loadfile":
        user_data           = loadfile.loadfile(input('Masukkan nama File User: ')) # user.csv
        wahana_data         = loadfile.loadfile(input('Masukkan nama File Daftar Wahana: ')) # wahana.csv
        pembelian_data      = loadfile.loadfile(input('Masukkan nama File Pembelian Tiket: ')) # pembelian.csv
        penggunaan_data     = loadfile.loadfile(input('Masukkan nama File Penggunaan Tiket: ')) # penggunaan.csv
        tiket_data          = loadfile.loadfile(input('Masukkan nama File Kepemilikan Tiket: ')) # tiket.csv
        refund_data         = loadfile.loadfile(input('Masukkan nama File Refund Tiket: ')) # refund.csv
        kritiksaran_data    = loadfile.loadfile(input('Masukkan nama File Kritik dan Saran: ')) #kritiksaran.csv
        print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
        
    if command =="loadfiletest":
        user_data           = loadfile.loadfile(input('Masukkan nama File user: '))

    if command == "signup":
        user_data = signup.signup(user_data)    
    
    if command == "exit":
        endprogram = True


#test
print(user_data)