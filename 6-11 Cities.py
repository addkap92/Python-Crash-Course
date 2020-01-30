cities = {
    'new york': {
        'country': 'usa',
        'population': '20,320,876',
        'fact': "New York City is made up of five boroughs: Manhattan, The Bronx, Queens, Brooklyn, and Staten Island.",
    },
    'los angeles': {
        'country': 'usa',
        'population': '3,990,456',
        'fact': "L.A. is the entertainment capital of the world"
    },
    'chicago': {
        'country': 'usa',
        'population': '2,705,994',
        'fact': "Chicago's nicknames include The Windy City, City of Big Shoulders, The Second City.",
    },
}

for citi, content in cities.items():
    print(citi.title())
    for item, value in content.items():
        if value == 'usa':
            print(item.title() + ": " + value.upper())
        else:
            print(item.upper() + ": " + value.title())
