my_pizzas = ['plain', 'pep', 'pineapple', 'grandma']
for pizza in my_pizzas:
    print("I like " + pizza)
print("I LOVE PIZZA!")
friends_pizza = my_pizzas[:]
my_pizzas.append('grandpa')
friends_pizza.append('sicilian')

print("My fav pizzas are: ")
for pizza in my_pizzas:
    print(pizza)
print("My friend's fav pizzas are: ")
for pizza in friends_pizza:
    print(pizza)