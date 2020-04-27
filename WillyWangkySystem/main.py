# Tugas Besar IF1210 Dasar Pemrograman
# Kelompok X

import F01_loadfile, F02_savefile, F03_signup, F04_login, F05_caripemain, F06_filterrides, F07_belitiket, F08_penggunaan, F09_refund, F10_givefeedback, F11_accessfeedback, F12_addride, F13_topup, F14_ridehistory, F15_ticketcount, F16_exit, B04_lostticket, B02_upgradegold, B03_wahanaterbaik, modules
'''
Zachrandika Alif Syahrzea
I Gede Govindabhakta
Ryandito Diandaru
Nabila Farras Ammara Mumtaz
Alvin Rizqi Alfisyahrin
'''

# KAMUS GLOBAL
'''
    user_data           : array of array of string
    wahana_data : array of array of string
    pembelian_data : array of array of string
    penggunaan_data : array of array of string
    tiket_data : array of array of string
    refund_data : array of array of string
    kritiksaran_data : array of array of string
    tikethilang_data : array of array of string
    endProgram : boolean
    currentUser : array of string
    i : integer
    data : array of array
    names : array of string
    command : string

'''
endprogram              = False
currentUser = [" $NOUSER", " %NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", "notLoggedIn", " $NOUSER"]

while (not endprogram):
    command = str(input("$ "))

    if command == "load":
        user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data = F01_loadfile.load()
        
    elif command == "autoload":
        user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data = F01_loadfile.autoLoad()

    elif command == "login":
        currentUser = F04_login.login(user_data)

    else:

        if currentUser[6] == " $NOUSER" :
            print("Silahkan login terlebih dahulu")

        else:
            if command == "save":
                data = [user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data]
                names = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran", "Tiket Hilang"]
                F02_savefile.save(data, names)

            elif command == "signup":
                user_data = F03_signup.signup(user_data, currentUser)    
    
            elif command == "cari_pemain":
                F05_caripemain.cari_pemain(currentUser, user_data)
    
            elif command == "cari":
                F06_filterrides.filterRides(wahana_data)
    
            elif command == "beli_tiket":
                pembelian_data, tiket_data, currentUser = F07_belitiket.beliTiket(pembelian_data, tiket_data, wahana_data, currentUser)
                modules.updateArray(user_data, currentUser, currentUser[3], 3)

            elif command == "main":
                F08_penggunaan.use_ticket(penggunaan_data, tiket_data, currentUser)
    
            elif command == "refund":
                F09_refund.refund(currentUser, tiket_data, refund_data, wahana_data)
    
            elif command == "kritik_saran":
                kritiksaran_data = F10_givefeedback.giveFeedback(kritiksaran_data, currentUser)
        
            elif command == "lihat_laporan":
                F11_accessfeedback.accessFeedback(kritiksaran_data)
    
            elif command == "tambah_wahana":
                wahana_data = F12_addride.addRide(wahana_data, currentUser)
    
            elif command == "topup":
                F13_topup.topup(user_data)
    
            elif command == "riwayat_wahana":
                F14_ridehistory.rideHistory(penggunaan_data, currentUser)
    
            elif command == "tiket_pemain":
                F15_ticketcount.showTicket(tiket_data, currentUser, wahana_data)

            elif command == "exit":
                simmpan = F16_exit.exit()
                if (simmpan):
                    data = [user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data]
                    names = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran", "Tiket Hilang"]
                    F02_savefile.save(data, names)
                endprogram = True
    
            elif command == "showdata" and currentUser[5] == "Admin" :
                data = [user_data, wahana_data, pembelian_data, penggunaan_data, tiket_data, refund_data, kritiksaran_data, tikethilang_data]
                for i in data:
                    print(i, end=" | ")
                    print("\n")
            
            elif command == "upgrade_gold":
                user_data = B02_upgradegold.upgradegold(user_data, currentUser)
            
            elif command == "best_wahana":
                B03_wahanaterbaik.showBestWahana(pembelian_data, wahana_data)

            elif command == "tiket_hilang":
                B04_lostticket.lostticket(tiket_data)   

            else:
                print("Command tidak dikenali, gunakan \"help\" untuk bantuan")
