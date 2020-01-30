numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(str(number) + " is the 1st")
    elif number == 2:
        print(str(number) + " is the 2nd")
    elif number == 3:
        print(str(number) + " is the 3rd")
    else:
        print(str(number) + " is the " + str(number) + "th")