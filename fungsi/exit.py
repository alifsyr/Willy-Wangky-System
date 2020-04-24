def exit():
    saev = input('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?')
    if saev == 'Y' or saev == 'y':
        return(True)   #return True berarti jalankan save
    elif saev == 'N' or saev == 'n':
        return(False)   #return false berarti jangan jalankan save
    #     return(user_data)   #array user_data yang habis diproses sama fungsi fungsi sebelumnya
    # elif saev == 'N' or saev 'n':
    #     return(arrayConstant)   #array A yang dibuat konstan di awal file
