def accessFeedback(feedback):
    import modules
    '''
    feedback 
    0 - Username
    1 - Tanggal kritik
    2 - ID Wahana
    3 - Isi Kritik
    '''
    feedback = modules.strSort(feedback, 2, "ascending")

    for entry in feedback:
        id_wahana   = entry[2]
        tanggal     = entry[1]
        user        = entry[0]
        kritik      = entry[3]
        print(id_wahana, tanggal, user, kritik, sep=" | ")