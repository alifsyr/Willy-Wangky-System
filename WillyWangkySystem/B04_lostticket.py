import csv

def lostTicket(x):
    user = input("Masukkan username: ")
    tanggal = input("Tanggal kehilangan tiket: ")
    ID = input("ID wahana: ")
    jumlah = int(input("Jumlah tiket yang dihilangkan: "))

    for i in x:
        if i[0] == user:
            i[3] = i[3]-jumlah

    with open('lostTicket.csv', mode='a') as tulisData:
        tulis = csv.writer(tulisData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tulis.writerow([user,tanggal,ID,jumlah]) 
