# Tugas Besar IF1210 Dasar Pemrograman
# Kelompok X

import F01_loadfile, F02_savefile, F03_signup, F04_login, F05_caripemain, F06_filterrides, F07_belitiket, F08_penggunaan, F09_refund, F10_givefeedback, F11_accessfeedback, F12_addride, F13_topup, F14_ridehistory, F16_exit, B04_lostticket
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
currentUser = [" $NOUSER", " %NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", "notLoggedIn", " $NOUSER"]

while (not endprogram):
    command = str(input("$ "))

    if command == "load":
        user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data = F01_loadfile.load()
        
    if command == "autoload":
        user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data = F01_loadfile.autoLoad()
    
    if command == "save":
        data = [user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data]
        names = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran"]
        F02_savefile.save(data, names)

    if command == "signup":
        F03_signup.signup(user_data, currentUser)    
    
    if command == "login":
        currentUser = F04_login.login(user_data)
    
    if command == "cari_pemain":
        F05_caripemain.cari_pemain(currentUser, user_data)
    
    elif command == "cari":
        F06_filterrides.filterRides(wahana_data)
    
    if command == "beli_tiket":
        pembelian_data, tiket_data = F07_belitiket.beliTiket(pembelian_data, tiket_data, wahana_data, currentUser)

    if command == "main":
        F08_penggunaan.use_ticket(penggunaan_data, tiket_data, currentUser)
    
    if command == "refund":
        F09_refund.refund(currentUser, tiket_data, refund_data, wahana_data)
    
    if command == "kritik_saran":
        kritiksaran_data = F10_givefeedback.giveFeedback(kritiksaran_data, currentUser)
        
    if command == "lihat_laporan":
        F11_accessfeedback.accessFeedback(kritiksaran_data)
    
    if command == "tambah_wahana":
        wahana_data = F12_addride.addRide(wahana_data, currentUser)
    
    if command == "topup":
        F13_topup.topup(user_data)
    
    elif command == "riwayat_wahana":
        F14_ridehistory.rideHistory(penggunaan_data, currentUser)
    
    if command == "tiket_pemain":
        print("Coming soon")

    if command == "exit":
        simmpan = F16_exit.exit()
        if (simmpan):
            data = [user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data]
            names = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran"]
            F02_savefile.save(data, names)
        endprogram = True
    
    else:
        print("HAH?")


#test
print(user_data)
