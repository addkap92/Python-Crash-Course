usernames = []
if usernames == []:
    print("Add some usernames!")
else:
    for name in usernames:
        if name.capitalize() == 'Admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print("Hello " + name + "," + "thank you for logging in again")


