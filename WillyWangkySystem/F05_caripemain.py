import csv
def cari_pemain(currentUser, user_data):
    import modules
    '''
    currentUser : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    '''
    found = False                                   # inisiasi
    if (currentUser[5] == "Admin"):                 # Hanya admin yang bisa mencari
        username = input('Masukkan username: ')     # input
        for row in user_data :                      # mengecek matriks user_data
            if username == row[3]:
                print("Nama Pemain: "+str(row[0]))
                print("Tinggi Pemain: "+str(row[2]))
                print("Tanggal Lahir Pemain :"+str(row[1]))
                found = True
        if not(found) :
            print('Pemain tidak ditemukan.')
    else:
        print("Maaf anda bukan Admin!")
