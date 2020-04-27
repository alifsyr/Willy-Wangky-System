import csv

def upgradegold(user_data,currentUser):    
    if currentUser[5] == "Admin":
        change_acc = input("Masukkan username yang ingin di-upgrade: ")     # Memberikan input username pemain
        for i in (user_data) :      # Melakukan looping pada matrix user_data
            if i[3] == change_acc:      # jika username tersedia
                if i[6] != "Saldo":       # Untuk memisahkan nama kolom dengan data
                    if int(i[6]) >= 100000:     # Jika saldo lebih atau sama dengan 100.000   
                        newSaldo = int(i[6]) - 100000
                        i[6] = str(newSaldo) 
                        i[5] = ("Gold")     # Role diubah menjadi Gold
                        print("Akun Anda telah diupgrade.")
                        return user_data
                    else:
                        print("Maaf saldo anda tidak cukup.")
    else:
        print("Maaf, anda bukan Admin.")                    