josephj= {
        'first_name': 'joseph',
        'last_name': 'jackson',
        'age': '24',
        'state': 'nj',
    }
aarona = {
        'first_name': 'aaron',
        'last_name': 'aloha',
        'age': '32',
        'state': 'ny',
    }
ryanr = {
        'first_name': 'ryan',
        'last_name': 'richard',
        'age': '24',
        'state': 'pa',
    }

people = [ryanr, aarona, josephj]


for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    print("\nPerson's name is: " + full_name.title() + ".")
    print("Age: " + str(person['age']))
    print("City: " + person['state'].title())