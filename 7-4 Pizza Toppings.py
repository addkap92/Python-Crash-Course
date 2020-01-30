# prompt = "\nTell me something and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. \t"
pizza_toppings = ""
while not(pizza_toppings == "quit" or pizza_toppings == "Quit"):
    message = input("What toppings would you like on your pizza?: ")

    if not(message == "quit" or message == "Quit"):
        print("Good choice! I'll add " + message + " to your pizza!")