def login():
        import csv
        success = False
        unameValid = False
        paswValid = False
        while not(success):
                uname = input('Masukkan username: ')
                pasw = input('Masukkan password: ')
                
                with open('user.csv') as user:
                        user_data = csv.reader(user, delimiter=',')
                        line_count = 0
                        for row in user_data:
                                if f'{row[3]}' == (uname):
                                        unameValid = True
                                if (unameValid):
                                        if f'{row[4]}' == (pasw):
                                                paswValid = True
                                                nama = f'{row[0]}'
                        if(paswValid):
                                print("Selamat bersenang-senang, "+nama)
                                return(True)
                        else:
                                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")

login()
