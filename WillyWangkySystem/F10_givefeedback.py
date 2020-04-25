import modules
def giveFeedback(kritiksaran_data, currentUser):
    ID_Wahana = input("Masukkan ID wahana: ")
    Tanggal_Kritik = input("Masukkan tanggal pelaporan: ")
    Isi_Kritik = input("Kritik/saran anda: ")
    print()
    FeedBack = [[str(currentUser[3]),  str(Tanggal_Kritik), str(ID_Wahana), str(Isi_Kritik)]]
    print("Kritik dan saran anda kami terima")
    kritiksaran_data = kritiksaran_data + FeedBack
    return (kritiksaran_data)
