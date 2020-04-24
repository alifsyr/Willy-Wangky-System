# Tugas Besar IF1210 Dasar Pemrograman
# Kelompok X

from fungsi import F01_loadfile, F02_savefile, F03_signup, F04_login, F05_caripemain, F06_filterrides, F07_belitiket, F08_penggunaan, F09_refund, F11_accessfeedback, F13_topup, F14_ridehistory, F16_exit, B04_lostticket
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
        user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data = F01_loadfile.load()
        
    elif command == "autoload":
        user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data = F01_loadfile.autoLoad()
    
    elif command == "save":
        data = [user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data]
        names = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran"]
        F02_savefile.save(data, names)

    elif command == "signup":
        F03_signup.signup(user_data, currentUser)    
    
    elif command == "login":
        currentUser = F04_login.login(user_data)
    
    elif command == "cari_pemain":
        print("Coming soon")
    
    elif command == "cari":
        print("Coming soon")
    
    elif command == "beli_tiket":
        pembelian_data, tiket_data = F07_belitiket.beliTiket(pembelian_data, tiket_data, wahana_data, currentUser)

    elif command == "main":
        print("Coming soon")
    
    elif command == "refund":
        print("Coming soon")
    
    elif command == "kritik_saran":
        print("Coming soon") 

    elif command == "lihat_laporan":
        print("Coming soon")
    
    elif command == "tambah_wahana":
        print("Coming soon")
    
    elif command == "topup":
        F13_topup.topup(user_data)
    
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