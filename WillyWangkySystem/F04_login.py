def login(user_data):
        #inisialisasi belum berhasil
        paswValid = False

        #input username dan password
        uname = input('Masukkan username: ')
        pasw = input('Masukkan password: ')

        #array dummy yang sama seperi di main
        dummy = [" $NOUSER", " %NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", "notLoggedIn", " $NOUSER"]

        #iterasi pengecekan username dan password
        for i in (user_data):
                if i[6] != 'Saldo':
                        if i[3] == uname:
                                if i[4] == pasw:
                                        #peng-valid an login, nama untuk di cetak dan currentUser u/ return
                                        paswValid = True
                                        nama = i[0]
                                        currentUser = i
  
        if(paswValid):
                print()
                print("Selamat bersenang-senang, "+nama)
                return(currentUser) #untuk indikasi login berhasil
        else:
                print()
                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
                return(dummy) #return array dummy
