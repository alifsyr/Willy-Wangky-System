def exit():
    #variabel untuk melakukan save atau tidak
    saev = input('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?')
    if saev == 'Y' or saev == 'y':
        return(True)   #return True berarti jalankan save
    elif saev == 'N' or saev == 'n':
        return(False)   #return false berarti jangan jalankan save
