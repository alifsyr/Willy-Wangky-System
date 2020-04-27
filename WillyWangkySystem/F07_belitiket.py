def beliTiket(pembelian_data, tiket_data, wahana_data,currentUser):
    import modules
    '''
    pembelian_data      : Username, Tanggal Pembelian, ID, Jumlah Tiket
    tiket_data          : Username, Tanggal Pembelian, ID, Jumlah Tiket
    wahana_data         : ID, Nama wahana, Harga tiket, Batasan umur, Batasan Tinggi
    currentUser         : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    '''

    # Input 
    inputIdWahana = str(input("Masukkan ID wahana: "))
    tanggal = str(input("Masukkan tanggal hari ini: "))
    jumlah = int(input("Jumlah tiket yang dibeli: "))

    idWahana = modules.search(inputIdWahana, 0, wahana_data, "index")

    # Validasi User and input
    if (modules.search(idWahana, 0, wahana_data, "boolean")):
        print("Wahana tidak ditemukan")
    elif (modules.umur(tanggal,currentUser[1]) < int(wahana_data[idWahana][3])):
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")
    elif (int(currentUser[2]) < int(wahana_data[idWahana][4])):
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.\nSilakan menggunakan wahana lain yang tersedia.")
    elif (int(currentUser[6]) < int(wahana_data[idWahana][2])):
        print("Saldo Anda tidak cukup\nSilakan mengisi saldo Anda")
    else:
        newPurchase = [str(currentUser[3]),  str(tanggal), str(idWahana), str(jumlah)]

        #Update saldo user
        newSaldo = int(currentUser[6]) - int(wahana_data[idWahana][2])

        currentUser[6] = newSaldo

        dataPembelianBaru = pembelian_data + newPurchase
        dataTiketBaru = tiket_data + newPurchase

        print("Selamat bersenang-senang di ", wahana_data[idWahana][1], ".", sep="")

        return dataPembelianBaru, dataTiketBaru, currentUser
    return pembelian_data, tiket_data, currentUser