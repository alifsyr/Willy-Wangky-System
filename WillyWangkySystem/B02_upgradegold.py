import csv

def upgrade_gold(x):    
    change_acc = input("Masukkan username yang ingin di-upgrade: ")
    for i in x :
        if i[3] == change_acc:
            i[5] = ("Gold")
        print("Akun Anda telah diupgrade.")
    