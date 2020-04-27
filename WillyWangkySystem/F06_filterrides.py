def filterRides(wahana_data):
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print()
    BatasUmur = int(input("Batasan umur pemain: "))
    #mengecek apakah input user valid
    while (BatasUmur<1 or BatasUmur>4):
        print("Batasan umur tidak valid!")
        BatasUmur = int(input("Batasan umur pemain: "))
    BatasTinggi = int(input("Batasan tinggi badan: "))
    while (BatasTinggi<1 or BatasUmur>3):
        print("Batasan tinggi badan tidak valid!")
        BatasTinggi = int(input("Batasan tinggi badan pemain: "))
    if (BatasUmur == 1):
        BU = "Anak-anak"
    elif (BatasUmur == 2):
        BU = "Dewasa"
    elif (BatasUmur == 3):
        BU = "Semua umur"
    if (BatasTinggi == 1):
        BT = ">=170 cm"
    else:
        BT = "Tanpa batasan"
    print()
    countride = 0 #untuk mengecek ketersediaan wahana
    print("Hasil pencarian")
    for i in (wahana_data):
        if (BU == i[3] and BT == i[4]): #memfilter wahana sesuai kriteria yang dimasukkan oleh user
            print(str(i[0] + " | " + i[1] + " | " + i[2]))
            countride = countride + 1
    if (countride == 0):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.") #wahana tidak tersedia
