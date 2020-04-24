import csv
def cari_pemain(currentUser, user_data):
    import modules
    '''
    currentUser : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    '''
    import module
    username = input('Masukkan username: ')
    found = False
    if (currentUser[5] == "Admin"):
        for row in user_data :
            if username == row[3]:
                print("Nama Pemain: "+str(user_data[0]))
                print("Tinggi Pemain: "+str(user_data[2]))
                print("Tanggal Lahir Pemain :"+str(user_data[1]))
                found = True
        if not(found) :
            print('Pemain tidak ditemukan.')
    else:
        print("Maaf anda bukan Admin!")
