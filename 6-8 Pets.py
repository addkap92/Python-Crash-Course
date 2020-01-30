# alfalfa = {
#     'breed': 'yorkie',
#     'owner': 'tom',
# }
#
# bear = {
#     'breed': 'bullnese',
#     'owner': 'jerry',
# }
#
# larry = {
#     'breed': 'australian sheep',
#     'owner': 'curly',
# }
# pets = [larry, bear, alfalfa]
#
# for dog in pets:
#     dog_info = dog['breed'] + dog['owner']
#     print(dog_info.title())


pets = [
    {
        'name': 'speedy',
        'breed': 'yorkie',
        'owner': 'larry',
    },
    {
        'name': 'terry',
        'breed': 'pitbull',
        'owner': 'axl',
    },
    {
        'name': 'gerry',
        'breed': 'golden retriever',
        'owner': 'jerry',
    },
]

for pet in pets:
    print(pet['name'].title() + " is a " + pet['breed'].title() + " and it's owner is " + pet['owner'].title())