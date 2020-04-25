tiket_data = [(0, 1), (2, 3), (0, 2), (5, 2), (0, 3)]
currentUser = [0, 0, 0, 0, 0, 0, 0]

def showTicket(tiket_data, currentUser):
    import modules

    for tiket in tiket_data:
        if tiket[0] == currentUser[3]:
            print(tiket[0], tiket[1], sep=" | ")

showTicket(tiket_data, currentUser)