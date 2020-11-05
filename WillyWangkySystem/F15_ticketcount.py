def showTicket(tiket_data, currentUser, wahana_data):

    '''
    tiket_data = Username,Tanggal_Pembelian,ID_Wahana,Jumlah_Tiket
    wahan_data = ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi
    '''

    import modules

    userTickets = []
    
    for row in tiket_data:
        if row[0] == currentUser[3]:
            userTickets = modules.addToArray(userTickets, row)
            
    userTickets = modules.strSort(userTickets, 2, "ascending")

    print("Riwayat: ")

    if modules.panjang(userTickets) != 0:
        selected = userTickets[0]
        currentCount = 0
    else:
        print()
        return

    for tiket in userTickets:
        if tiket[2] == selected[2]:
            currentCount += int(tiket[3])
        else:
            rideIndex = modules.search(selected[2], 0, wahana_data, 'index')
            rideName = wahana_data[rideIndex][1]
            print(selected[2], rideName, currentCount, sep=" | ")
            lastcount = currentCount
            currentCount = 0
            selected = tiket
    
    rideIndex = modules.search(selected[2], 0, wahana_data, 'index')
    rideName = wahana_data[rideIndex][1]
    print(tiket[2], rideName, lastcount, sep=" | ")