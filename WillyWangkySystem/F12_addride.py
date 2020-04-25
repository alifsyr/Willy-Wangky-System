import modules
def addRide(wahana_data,currentUser):
    if (currentUser[5] != "Admin"):
        print("Anda tidak mendapat izin untuk mengakses fungsi ini.")
    else:
        print("Masukkan informasi wahana yang ditambahkan:")
        ID_Wahana = input("Masukkan ID wahana: ")
        Nama_Wahana = input("Masukkan nama wahana: ")
        Harga_Tiket = input("Masukkan harga tiket: ")
        Batasan_Umur = input("Batasan umur: ")
        Batasan_Tinggi = input("Batasan tinggi badan: ")
        print()
        WahanaBaru = [[str(ID_Wahana),  str(Nama_Wahana), str(Harga_Tiket), str(Batasan_Umur), str(Batasan_Tinggi)]]
        print("Info wahana telah ditambahkan!"
        wahana_data = wahana_data + WahanaBaru
        return wahana_data
