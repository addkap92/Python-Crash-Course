question = True

while question:
    message = input("How old is the movie-goer? \nIf you have nothing else to check enter Quit\n")
    if message == 'quit' or message == 'Quit':
        question = False
    elif int(message) < 3:
        print("The ticket is free!")
    elif int(message) >= 3 and int(message) < 12:
        print("The ticket is $10!")
    elif int(message) >= 12:
        print("The ticket is $15!")
