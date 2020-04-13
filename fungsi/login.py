def login(x):

        success = False
        unameValid = False
        paswValid = False
        i = 0

        while not(success):
                uname = input('Masukkan username: ')
                pasw = input('Masukkan password: ')

                while i < len(x) and not(paswValid):
                        if x[i][3] == uname:
                                unameValid = True
                                if(unameValid):
                                        if x[i][4] == pasw:
                                                paswValid = True
                        else:
                                i += 1
                if(paswValid):
                        print("Selamat bersenang-senang, "+x[i][0])
                        return(True) #untuk indikasi login berhasil
                else:
                        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
