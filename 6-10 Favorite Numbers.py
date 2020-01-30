favnumbers = {'mike': [22, 21, 20],
              'joe': [23, 32],
              'sam': [11, 10, 9],
              'lex': [32, 23],
              'al': [12, 21]
              }

for person, numbers in favnumbers.items():
    print(person.title() + "'s favorite numbers are: " + str(numbers))
    #print(numbers)