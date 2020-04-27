def showBestWahana(pembelian_data, wahana_data):

    '''
    pembelian_data = Username,Tanggal_Pembelian,ID_Wahana,Jumlah_Tiket
    wahana_data = ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi
    '''

    import modules

    pembelian_data = modules.strSort(pembelian_data, 2, "ascending")

    pembelian_wahana = []

    if modules.panjang(pembelian_data) != 0:
        selected = pembelian_data[1]
        currentCount = 0
    else:
        print()
        return
        
    wahanaCount = 0

    for data in pembelian_data:
        if data != pembelian_data[0]:
            if data[2] == selected[2]:
                currentCount += int(data[3])
                

            else:
                # Memberi input baru pembelian data
                # Input baru berisi ID Wahana dan jumlah tiket total (currentCount)
                newEntry = [selected[2], currentCount]
                pembelian_wahana = modules.addToArray(pembelian_wahana, newEntry)
                wahanaCount += 1

                selected = data
                currentCount = int(selected[3])
            

    # Menambahkan data terakhir
    newEntry = [data[2], int(currentCount)]
    pembelian_wahana = modules.addToArray(pembelian_wahana, newEntry)

    pembelian_wahana = modules.intSort(pembelian_wahana, 1, "descending")

    count = 0
    while count <=2 and count <= wahanaCount:
        indexWahana = modules.search(pembelian_wahana[count][0], 0, wahana_data, "index")
        namaWahana = wahana_data[indexWahana][1]
        print(count+1 , pembelian_wahana[count][0], namaWahana, pembelian_wahana[count][1], sep=" | ")
        count += 1