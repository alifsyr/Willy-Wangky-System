def showTicket(tiket_data, currentUser):
    for tiket in tiket_data:
        if tiket[0] == currentUser[3]:
            print()