import csv
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
    jumlah_tiket = input('Jumlah tiket yang digunakan: ')
    username = currentUser[3]
    if id_wahana == tiket_data[username][1] and jumlah_tiket <= tiket_data[username][2] :
                print('Terimakasih telah bermain.')
                newPenggunaan = (str(currentUser[3]), str(tanggal), str(id_wahana), str(jumlah_tiket))
                newKepemilikan = (str(currentUser[3]), str(id_wahana), str(tiket_data[id_wahana][3] - jumlah_tiket))
                return penggunaan_data + newPenggunaan, tiket_data + newKepemilikan
    else:
        print('Tiket Anda tidak valid dalam sistem kami')
