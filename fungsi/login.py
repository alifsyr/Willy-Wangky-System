def login(x):
        global role
        paswValid = False
        
        while not(paswValid):
                uname = input('Masukkan username: ')
                pasw = input('Masukkan password: ')
                
                for i in x:
                        if i[3] != 'Username':
                                if i[3] == uname:
                                    if i[4] == pasw:
                                        paswValid = True
                                        nama = i[0]
                                        role = i[5]
                    
                if(paswValid):
                        print("Selamat bersenang-senang, "+nama)
                        return(True) #untuk indikasi login berhasil
                else:
                        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
