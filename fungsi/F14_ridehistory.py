def rideHistory(penggunaan_data):
    ID = input("Masukkan ID wahana: ")
    print("Riwayat:")
    for i in (penggunaan_data):
        if ID == i[2]:
            print(str(i[1]) + " | " + str(i[0]) + " | " + str(i[3]))
