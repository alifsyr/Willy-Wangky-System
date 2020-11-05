
def use_ticket(penggunaan_data, tiket_data, currentUser):
    import modules
    '''
    pembelian_data : Username, Tanggal Pembelian, ID, Jumlah Tiket
    penggunaan_data : Username, Tanggal Penggunaan, ID Wahana, Jumlah Tiket
    currentUser : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    tiket_data : username, id wahana, jumlah tiket
    '''
    id_wahana =  input('Masukkan ID Wahana: ')                      #input
    tanggal = input('Masukkan tanggal hari ini: ')
    jumlah_tiket = int(input('Jumlah tiket yang digunakan: '))
    username = str(currentUser[3])                                  #memakai data user yang login
    found = False
    for row in tiket_data:                                          #loop matriks
        if row[0] == username :
            if id_wahana == row[1] and jumlah_tiket <= int(row[2]): #jika input lebih kecil dari tiket yang dimiliki maka valid
                found = True
                print('Terimakasih telah bermain.')
                newPenggunaan = [str(currentUser[3]), str(tanggal), str(id_wahana), str(jumlah_tiket)]  #mengisi data tambahan di file penggunaan
                row[2] = str(int(row[2])-(jumlah_tiket))    #mengubah data kepemilikan tiket
                return penggunaan_data + newPenggunaan
    if not(found) :
        print('Tiket Anda tidak valid dalam sistem kami')
