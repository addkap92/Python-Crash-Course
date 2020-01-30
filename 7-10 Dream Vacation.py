responses = {}
while True:
    name = input("What is your name?\n")
    place = input("What is your dream vacation?\n")
    responses[name] = place

    response = input("Does anyone else want to answer?\n")
    if response == 'no':
        break
for name, place in responses.items():
    print(name.title() + "'s dream vacation is to go to " + place.title())