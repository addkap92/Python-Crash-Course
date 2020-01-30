car = input("What kind of car would you like to rent? ")
if car.capitalize() == 'subaru' or car == 'subaru':
    print("Excellent! We have that in stock")
else:
    print("Sorry, that car is not available")