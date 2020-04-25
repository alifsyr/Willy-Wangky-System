def rideHistory(penggunaan_data, currentUser):
    if (currentUser[5] != "Admin"):
        print("Anda tidak mendapat izin untuk mengakses fungsi ini.")
    else:
        ID = input("Masukkan ID wahana: ")
        print("Riwayat:")
        for i in (penggunaan_data):
            if ID == i[2]:
                print(str(i[1]) + " | " + str(i[0]) + " | " + str(i[3]))
