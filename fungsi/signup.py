import csv

user_data = []

def signup():
    while True:
        for row in user_data:
            if f'{row[5]}' == "Admin":
                with open('user.csv',mode='a') as sign_up:
                    print("STOP GIVING ME ERRORS")