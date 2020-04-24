import csv
import modules

# type user : (Nama : string, Tinggi_Badan : string, Tanggal_Lahir : string, username : string)
# data : SEQFILE of data_pemain
# data_pemain : user
def EOP(x) :
    return ( x[0] == mark[0] and x[1] == mark[1] and x[2] == mark[2] and x[3] == mark[3])


def cari_pemain():
    username = input('Masukkan username: ')
    data_pemain = csv.reader(open('user.csv', "rb"), delimiter=",")
    found = False
    for row in data_pemain :
        if username == row[3]:
            print(row)
            found = True
    if not(found) :
        print('Pemain tidak ditemukan.')
