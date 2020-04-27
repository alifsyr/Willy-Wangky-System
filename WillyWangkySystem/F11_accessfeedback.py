
def accessFeedback(feedback):
    from modules import strSort
    '''
    feedback 
    0 - Username
    1 - Tanggal kritik
    2 - ID Wahana
    3 - Isi Kritik
    '''
    feedback = strSort(feedback, 2, "ascending")

    print("Kritik dan saran: ")
    for entry in feedback:
        if entry != feedback[0]:
            id_wahana   = entry[2]
            tanggal     = entry[1]
            user        = entry[0]
            kritik      = entry[3]
            print(id_wahana, tanggal, user, kritik, sep=" | ")