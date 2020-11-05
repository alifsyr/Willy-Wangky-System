def updatearray(file, new_value, who, who_index, what_index):
    #file : nama array yang ingin diubah
    #new_value : nilai baru yang ingin diupdate
    #who : datanya
    #who index : data 'who' itu indeksnya keberapa
    #what_index : data 'what' itu indeks keberapa
    for i in file:
        if i[who_index] == who:
            i[what_index] = new_value

arrayTest = [['end',4,5],
        ['my',7,4],
        ['suffering',8,5]]

who_to_change = 'end'

updatearray(arrayTest, 500, who_to_change, 0, 2)

for j in arrayTest:
    print(j)
    
