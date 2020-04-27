# user_data = [["0", "0", "0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1", "1", "1"]]

def signup(user_data, currentUser):
    import modules
    unameAvailable = False      # Inisiasi
    role = currentUser[5]
    new_data = [0 for i in range (7)]
    i = 0
    if (role == "Admin"):    # Validasi role apakah Admin atau Pemain
        new_data[0]   = input("Masukkan nama pemain: ")      # Memberikan input nama pemain
        new_data[1]   = input("Masukkan tanggal lahir pemain: ")    # Memberikan input tanggal lahir pemain
        new_data[2]   = input("Masukkan tinggi badan pemain (cm):  ")    # Memberikan input tinggi pemain dalam cm 
        new_data[3]   = input("Masukkan username pemain: ")     # Memberikan input username pemain 
        while  i < (modules.panjang(user_data)) and not(unameAvailable):       # Program terus mengulang pada saat panjang array user_data kurang dari i dan unameAvailable False 
            if user_data[i][3] == new_data[3]:      # Jika username sudah digunakan    
                print("Username sudah digunakan, silahkan masukan username lain.")
                new_data[3]   = input("Masukkan username pemain: ")
            else:   
                    i += 1      
                    
        new_data[4]   = input("Masukkan password pemain: ")     # Memberika input password 
        new_data[5]   = ("Pemain")      
        new_data[6]   = ("0")
        print("Selamat menjadi pemain,",new_data[0],". Selamat bermain.")
        user_data = user_data + [new_data]      # array new_data ditambahkan kedalam array user_data
        return user_data
    else:
        print("Maaf anda bukan Admin !")  

# x = [(0), (0), (0)]
# currentUser = [" $NOUSER", " %NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", "Admin", " $NOUSER"]
# signup(x, currentUser)