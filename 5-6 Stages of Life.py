age = int(input("What is your age?\n"))
if age < 2:
    print("You're a baby!")
elif (age == 2) or (age < 4):
    print("You're a toddler!")
elif (age == 4) or (age < 13):
    print("You're a kid!")
elif (age == 13) or (age < 20):
    print("You're a teenager!")
elif (age == 20) or (age < 65):
    print("You're a adult!")
elif age >= 65:
    print("You're a senior!")