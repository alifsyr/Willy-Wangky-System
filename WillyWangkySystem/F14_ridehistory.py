def rideHistory(penggunaan_data, currentUser):
    if (currentUser[5] != "Admin"): #mengecek apakah user merupakan admin atau bukan
        print("Anda tidak mendapat izin untuk mengakses fungsi ini.")
    else:
        ID = input("Masukkan ID wahana: ")
        print("Riwayat:")
        for i in (penggunaan_data):
            if ID == i[2]: #mencari wahana yang dimaksud
                print(str(i[1]) + " | " + str(i[0]) + " | " + str(i[3]))
