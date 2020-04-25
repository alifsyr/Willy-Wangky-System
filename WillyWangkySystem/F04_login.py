def login(user_data):
        
        paswValid = False


        while not(paswValid):
                uname = input('Masukkan username: ')
                pasw = input('Masukkan password: ')
                
                for i in (user_data):
                        if i[6] != 'Saldo':
                                if i[3] == uname:
                                    if i[4] == pasw:
                                        paswValid = True
                                        nama = i[0]
                                        currentUser = i
                    
                if(paswValid):
                        print("Selamat bersenang-senang, "+nama)
                        return(currentUser) #untuk indikasi login berhasil
                else:
                        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
