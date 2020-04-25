def refund(currentUser, tiket_data, refund_data, wahana_data):
    import modules
    '''
    currentUser : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    tiket_data : username, id wahana, jumlah tiket
    refund_data : username, tanggal refund, id wahana, jumlah tiket
    wahana_data : ID, Nama wahana, Harga tiket, Batasan umur, Batasan Tinggi
    '''
    id_wahana = input('Masukkan ID Wahana: ')                   #input
    tanggal = input('Masukkan tanggal refund: ')
    jumlah_refund = int(input('Jumlah tiket yang di refund: '))
    username = currentUser[3]                                   #memakai data user yang login sekarang
    found = False
    if currentUser[5] == 'Pemain' or currentUser[5] == 'Gold' : #admin tidak bisa refund
        for row in tiket_data:                                  #loop matriks
            if row[0] == username:
                if id_wahana == row[1] and jumlah_refund <= int(row[2]):    #id harus valid dan jumlah tiket yang direfund harus lebih kecil dari yang dimiliki
                    found = True
                    print('Uang refund sudah kami berikan pada akun Anda.')
                    newRefund = [str(currentUser[3]), str(tanggal), str(id_wahana), str(jumlah_refund)] #mengisi data di refund
                    row[2] = str(int(row[2])-(jumlah_refund))   #mengubah data kepemilikan tiket
                    for i in wahana_data:
                        if id_wahana == i[0]:
                            if currentUser[5] == 'Pemain' :     #Jika gold, maka refund berkurang setengah
                                currentUser[6] = str(int(currentUser[6]) + ((int(i[2])/10)*(jumlah_refund)))
                            else:
                                currentUser[6] = str(int(currentUser[6]) + ((int(i[2])/20)*(jumlah_refund)))
                    return refund_data + newRefund
        if not(found) :
            print('Tiket anda tidak valid dalam data kami')
