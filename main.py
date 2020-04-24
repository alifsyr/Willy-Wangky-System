# Tugas Besar IF1210 Dasar Pemrograman
# Kelompok X

from fungsi import loadfile, login, signup, savefile, belitiket, accessfeedback

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
currentUser = [" $NOUSER", " %NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", "notLoggedIn", " $NOUSER"]

while (not endprogram):
    command = str(input("$ "))

    if command == "load":
        user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data = loadfile.load()
        
    elif command == "loadfiletest":
        user_data = loadfile.loadfile(input('Masukkan nama File user: '))
    
    elif command == "save":
        data = [user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data]
        names = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran"]
        savefile.save(data, names)

    elif command == "signup":
        user_data = signup.signup(user_data, currentUser)    
    
    elif command == "login":
        currentUser = login.login(user_data)
    
    elif command == "cari_pemain":
        print("Coming soon")
    
    elif command == "cari":
        print("Coming soon")
    
    elif command == "beli_tiket":
        pembelian_data, tiket_data = belitiket.beliTiket(pembelian_data, tiket_data, wahana_data, currentUser)

    elif command == "main":
        print("Coming soon")
    
    elif command == "refund":
        print("Coming soon")
    
    elif command == "kritik_saran":
        accessfeedback.accessFeedback(kritiksaran_data)

    elif command == "lihat_laporan":
        print("Coming soon")
    
    elif command == "tambah_wahana":
        print("Coming soon")
    
    elif command == "topup":
        print("Coming soon")
    
    elif command == "riwayat_wahana":
        print("Coming soon")
    
    elif command == "tiket_pemain":
        print("Coming soon")

    elif command == "exit":
        endprogram = True
    
    else:
        print("HAH?")


#test
print(user_data)