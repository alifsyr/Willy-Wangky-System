def topUp(user_data):
    uname = input('Masukkan username: ')
    tambah = int(input('Masukkan saldo yang di-top up: '))
    for i in (user_data):
        if i[6] != 'Saldo':
            if i[3] == uname:
                nama = i[0]
                i[6] = i[6] + tambah
                saldo = i[6]
    print()
    print("Top up berhasil. Saldo "+nama+" bertambah menjadi "+str(saldo))
