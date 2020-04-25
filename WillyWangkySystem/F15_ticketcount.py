def showTicket(tiket_data, currentUser):

    for tiket in tiket_data:
        if tiket[0] == currentUser[3] and (tiket != tiket_data[0]):
            print(tiket[0], tiket[1], sep=" | ")