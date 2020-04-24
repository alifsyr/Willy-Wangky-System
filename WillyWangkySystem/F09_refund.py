
import csv

def refund(currentUser, tiket_data, refund_data, wahana_data):
    import modules
    '''
    currentUser : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    tiket_data : username, tanggal pembelian,id wahana, jumlah tiket
    refund_data : username, tanggal refund, id wahana, jumlah tiket
    wahana_data : ID, Nama wahana, Harga tiket, Batasan umur, Batasan Tinggi
    '''
    id_wahana = input('Masukkan ID Wahana: ')
    tanggal = input('Masukkan tanggal refund: ')
    jumlah_refund = input('Jumlah tiket yang di refund: ')
    username = currentUser[3]
    if id_wahana != tiket_data[username][1] or jumlah_refund > tiket_data[username][2]:
        print('Anda tidak memiliki tiket terkait')
    elif id_wahana == tiket_data[username][1] or jumlah_refund <= tiket_data[username][2]:
        print('Uang refund sudah kami berikan pada akun Anda.')
        newRefund = (str(currentUser[3]), str(tanggal), str(id_wahana), str(tiket_data[username][2]-jumlah_refund))
        newKepemilikan = (str(currentUser[3]), str(id_wahana), str(tiket_data[id_wahana][2] - jumlah_refund))
        currentUser[6] = currentUser[6] - (((wahana_data[id_wahana][2])/10)*jumlah_refund)
        return refund_data + newRefund, tiket_data + newKepemilikan
