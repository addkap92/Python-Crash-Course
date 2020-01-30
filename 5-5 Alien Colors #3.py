alien_color = ['green', 'yellow', 'red']
color = input("An alien was just shot down! What color was it?\n")
if color == 'green':
    print("You got 5 points!")
elif color == 'yellow':
    print("You got 10 points!")
elif color == 'red':
    print("You got 15 points!")
else:
    print("Hmmm that doesn't sound like an alien...try again")
