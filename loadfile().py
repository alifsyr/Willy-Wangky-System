def loadfile(x):
    import csv
    with open(x) as csvfile :
        loadFile= csv.reader (csvfile, delimiter=',')
loadfile(input('Masukan nama File User: '))
loadfile(input('Masukan nama File Daftar Wahana: '))
loadfile(input('Masukan nama File Pembelian Tiket: '))
loadfile(input('Masukan nama File Penggunaan Tiket: '))
loadfile(input('Masukkan nama File Kepemilikan Tiket: '))
loadfile(input('Masukkan nama File Refund Tiket: '))
loadfile(input('Masukkan nama File Kritik dan Saran: '))

print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")