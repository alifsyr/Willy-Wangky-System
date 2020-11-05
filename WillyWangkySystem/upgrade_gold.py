import csv

def upgrade_gold():    
    change_acc = input("Masukkan username yang ingin di-upgrade: ")
    for i in user_data:
        if i[3] == change_acc:
            i[5] = ("Gold")
        print("Akun Anda telah diupgrade.")
    return user_data