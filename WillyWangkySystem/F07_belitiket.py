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
        print("No ride like that homie")
    elif (modules.umur(tanggal,currentUser[1]) < int(wahana_data[idWahana][3])):
        print("Too fucking young")
    elif (int(currentUser[2]) < int(wahana_data[idWahana][4])):
        print("Too fucking short")
    elif (int(currentUser[6]) < int(wahana_data[idWahana][2])):
        print("Where's my fucking money")
    else:
        newPurchase = [str(currentUser[3]),  str(tanggal), str(idWahana), str(jumlah)]

        #Update saldo user
        newSaldo = int(currentUser[6]) - int(wahana_data[idWahana][2])

        currentUser[6] = newSaldo

        dataPembelianBaru = pembelian_data + newPurchase
        dataTiketBaru = tiket_data + newPurchase

        return dataPembelianBaru, dataTiketBaru, currentUser
    return pembelian_data, tiket_data, currentUser