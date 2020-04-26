import csv

def upgrade_gold(user_data):    
    change_acc = input("Masukkan username yang ingin di-upgrade: ")
    for i in (user_data) :
        if i[3] == change_acc:
            if i[6] != "Saldo":
                if int(i[6]) >= 100000:
                    int(i[6]) - 100000
                    i[5] = ("Gold")
                    print("Akun Anda telah diupgrade.")
                else:
                    print("Maaf saldo anda tidak cukup.")