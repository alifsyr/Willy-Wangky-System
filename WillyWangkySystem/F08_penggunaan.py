
def use_ticket(penggunaan_data, tiket_data, currentUser):
    import modules
    '''
    pembelian_data : Username, Tanggal Pembelian, ID, Jumlah Tiket
    penggunaan_data : Username, Tanggal Penggunaan, ID Wahana, Jumlah Tiket
    currentUser : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    tiket_data : username, id wahana, jumlah tiket
    '''
    id_wahana =  input('Masukkan ID Wahana: ')
    tanggal = input('Masukkan tanggal hari ini: ')
    jumlah_tiket = int(input('Jumlah tiket yang digunakan: '))
    username = str(currentUser[3])
    found = False
    for row in tiket_data:
        if row[0] == username :
            if id_wahana == row[1] and jumlah_tiket <= int(row[2]):
                found = True
                print('Terimakasih telah bermain.')
                newPenggunaan = [str(currentUser[3]), str(tanggal), str(id_wahana), str(jumlah_tiket)]
                newKepemilikan = [str(currentUser[3]), str(id_wahana), str(int(row[2]) - jumlah_tiket)]
                return penggunaan_data + newPenggunaan, tiket_data + newKepemilikan
    if not(found) :
        print('Tiket Anda tidak valid dalam sistem kami')
