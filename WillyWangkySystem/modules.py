'''
MODULES.PY

panjang             | 10 
intSort             | 25
strSort             | 48
eOrde               | 86
umur                | 119
dateFormat          | 133
'''

def panjang(x):
    len = 0
    for i in x:
        len  = len + 1
    return(len)  
    
# test = [[1,2], [2,3], [1,3], [4,2], [2,3]]
# testText = [("ABC", 2), ("BcA", 3), ("Aad", 1)]
### Sort
'''
database        : array, urutkan array ini
column          : int, berdasarkan kolom ini
order           : string, 'ascending' atau 'descending'
'''

def intSort(database, column, order):
    for i in range(panjang(database)):
        # Mengurutkan data berdasarkan kolom berisi integer
        if (i > 0):
            current = i
            selected = i-1
            
            if (order == "ascending"):
                while (int(database[current][column]) < int(database[selected][column]) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1
            else:
               while (int(database[current][column]) > int(database[selected][column]) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1 
    return database

def strSort(database, column, order):
    for i in range(panjang(database)):
        # Mengurutkan data berdasarkan kolom berisi integer
        if (i > 0):
            current = i
            selected = i-1
            
            if (order == "ascending"):
                while ((stringOrder(database[current][column], database[selected][column])) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1
            else:
               while ((stringOrder(database[current][column], database[selected][column])) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1 
    return database

def stringOrder(stringA, stringB):
    lenA = panjang(stringA)
    lenB = panjang(stringB)
    if lenA < lenB:
        length = lenA
    else:
        length = lenB

    i = 0
    for i in range(length):
        if eOrde(stringA[i]) != eOrde(stringB[i]):
            return eOrde(stringA[i]) < eOrde(stringB[i])
    return lenA < lenB


def eOrde(char):
    '''
    ASCII for integer       : 48-57
    ASCII for uppercase     : 65-90
    ASCII for lowercase     : 97-122
    ASCII for specials      : 33-47, 58-64, 91-96, 123-126
    ASCII for space         : 32 (considered special)

    converted to
    specials                : 32-47, 48-53, 54-59, 60-63
    integer                 : 64-73
    character               : 74-99 (selang-seling a dan A)
    '''
    orde = ord(char)

    integer     = (orde >= 48 and orde <= 57)
    uppercase   = (orde >= 65 and orde <= 90)
    lowercase   = (orde >= 97 and orde <= 122)
    specials1   = (orde >= 32 and orde <= 47)
    specials2   = (orde >= 59 and orde <= 64)
    specials3   = (orde >= 91 and orde <= 96)
    specials4   = (orde >= 123 and orde <= 126)

    if      specials1:  return orde
    elif    specials2:  return orde-11
    elif    specials3:  return orde-37
    elif    specials4:  return orde-63
    elif    integer:    return orde+16
    elif    uppercase:  return 75+2*(orde-65)
    elif    lowercase:  return 74+2*(orde-97)
    else: return 100

def umur(today, born):
    sekarang    = dateFormat(today)
    lahir       = dateFormat(born)

    umur = sekarang[2] - lahir[2]

    if (sekarang[1] > lahir[1]):
        umur += 1
    elif (sekarang[1] == lahir[1] and sekarang[0] >= lahir[0]):
        umur += 1

    return umur

def dateFormat(date):
    '''
    format tanggal hari_ini dan ulang_tahun
    dd/mm/yyyy
    '''
    hari    = int( date[0] + date[1] )
    bulan   = int( date[3] + date[4] )
    tahun   = int( date[6] + date[7] + date[8] + date[9] )
    return (hari, bulan, tahun)

def search(data, query, file, option):
    # data : bentuk data yang dicari
    # query : jenis data ( dalam row apa )
    # file : nama file
    # option : pilihan ada dua, 'boolean' atau 'print',
    # jika memilih print maka akan menampilkan row yang dicari
    # contoh : search("babi", username, user_data, boolean)
    if option == 'boolean' :
        for row in file :
            if data == row[query] :
                return True
            else:
                return False
    elif option == 'print':
        for row in file :
            if data == row[query] :
                print(row)
