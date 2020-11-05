import modules
def giveFeedback(kritiksaran_data, currentUser):
    if (currentUser[5] != "Pemain"): #mengecek apakah user merupakan pemain atau bukan
        print("Anda tidak mendapat izin untuk mengakses fungsi ini.")
    else:
        ID_Wahana = input("Masukkan ID wahana: ")
        Tanggal_Kritik = input("Masukkan tanggal pelaporan: ")
        Isi_Kritik = input("Kritik/saran anda: ")
        print()
        FeedBack = [[str(currentUser[3]),  str(Tanggal_Kritik), str(ID_Wahana), str(Isi_Kritik)]]
        print("Kritik dan saran anda kami terima")
        kritiksaran_data = kritiksaran_data + FeedBack #update database kritik saran
    return (kritiksaran_data)
