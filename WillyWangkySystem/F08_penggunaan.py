import csv

# type user : (Nama : string, Tinggi_Badan : string, Tanggal_Lahir : string, username : string)
# data : SEQFILE of data_pemain
# data_pemain : user

def use_ticket():
    import modules

    id_wahana =  input('Masukkan ID Wahana: ')
    tanggal = input('Masukkan tanggal hari ini: ')
    jumlah_tiket = input('Jumlah tiket yang digunakan: ')
    found = False
    for row in pembelian_data:
        if id_wahana == row[2] and tanggal == row[1] :
            if jumlah_tiket <= row[3]:
                print('Terimakasih telah bermain.')
                found = True
            else:
                print('Tiket Anda tidak valid dalam sistem kami')
    if not(found):
        print('Tiket Anda tidak valid dalam sistem kami')
                
