my_foods = ['pizza', 'falafel', 'cake']
friends_food = my_foods[:]

my_foods.append('lettuce')
friends_food.append('carrots')

print("My fav foods are: ")
for food in my_foods:
    print(food)

print("\nMy friend's fav foods are: ")
for food in friends_food:
    print(food)