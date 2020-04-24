import csv
import modules

# type user : (Nama : string, Tinggi_Badan : string, Tanggal_Lahir : string, username : string)
# data : SEQFILE of data_pemain
# data_pemain : user

def refund():
    id_wahana = input('Masukkan ID Wahana: ')
    tanggal = input('Masukkan tanggal refund: ')
    jumlah_refund = input('Jumlah tiket yang di refund: ')
    found = False
    for row in pembelian_data:
        if id_wahana == row[2] and tanggal == row[1] :
            if jumlah_refund <= row[3]:
                print('Uang refund sudah kami berikan pada akun anda')
                found = True
            else :
                print('Anda tidak memiliki tiket terkait')
    if not(found):
        print('Anda tidak memiliki tiket terkait')
