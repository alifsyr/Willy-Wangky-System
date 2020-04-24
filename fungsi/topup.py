def topup(user_data):
    uname = input('Masukkan username: ')
    tambah = int(input('Masukkan saldo yang di-top up: '))
    for i in (user_data):
        if i[6] != 'Saldo':
            if i[3] == uname:
                nama = i[0]
                i[6] = int(i[6]) + tambah
                saldo = i[6]
    print()
    print("Top up berhasil. Saldo "+nama+" bertambah menjadi "+str(saldo))


#ignore, ini buat ngetes
aa = [['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password','Role','Saldo'],
      ['Babi','12/12/2001',170,'babiman','XXXXXX','Admin',0],
      ['Kucing','12/04/2020',45,'kucingman','sukasarden123','Admin',0],
      ['Bebek','12/04/2020',45,'bebekman','kweks','Pemain',99]]

