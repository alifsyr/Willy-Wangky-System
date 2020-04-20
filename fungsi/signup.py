import csv

def signup(user_data):
    success = False
    unameAvailable = False
    global new_data
    new_data = [0 for i in range (6)]
    i = 0
    while not(success):
        for i in new_data:
            new_data[0]   = input("Masukkan nama pemain: ")
            new_data[1]   = input("Masukkan tanggal lahir pemain: ")
            new_data[2]   = int(input("Masukkan tinggi badan pemain (cm):  "))
            new_data[3]   = input("Masukkan username pemain: ")
            while  i < len(user_data) and not(unameAvailable):
                        if user_data[i][3] == new_data[3]: 
                            print("Username sudah digunakan, silahkan masukan username lain.")
                            new_data[3]   = input("Masukkan username pemain: ")
                               
                        else:
                                i += 1
            new_data[4]   = input("Masukkan password pemain: ")
            new_data[5]   = ("pemain")
            return new_data
                    