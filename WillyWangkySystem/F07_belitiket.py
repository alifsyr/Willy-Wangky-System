def beliTiket(pembelian_data, tiket_data, wahana_data,currentUser):
    import modules
    '''
    pembelian_data      : Username, Tanggal Pembelian, ID, Jumlah Tiket
    tiket_data          : Username, Tanggal Pembelian, ID, Jumlah Tiket
    wahana_data         : ID, Nama wahana, Harga tiket, Batasan umur, Batasan Tinggi
    currentUser         : Nama, Tanggal Lahir, Tinggi, Username, Password, Role, Saldo
    '''

    # Input 
    idWahana = int(input("Masukkan ID wahana: "))
    tanggal = str(input("Masukkan tanggal hari ini: "))
    jumlah = int(input("Jumlah tiket yang dibeli: "))


    # Validasi User
    if (modules.umur(tanggal,currentUser[1]) < wahana_data[idWahana][3]):
        print("Too fucking young")
    elif (int(currentUser[2]) < wahana_data[idWahana][4]):
        print("Too fucking short")
    elif (int(currentUser[6] < wahana_data[idWahana][2])):
        print("Where's my fucking money")
    else:
        newPurchase = (str(currentUser[3]),  str(tanggal), str(idWahana), str(jumlah))
        return pembelian_data + newPurchase, tiket_data + newPurchase 
