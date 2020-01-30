def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Add The Great to each Magician"""
    # create new list to store The Great Magicians
    great_magicians = []

    # Make each magician great and add them to great_magician
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' The Great'
        great_magicians.append(great_magician)
    for magician in great_magicians:
        print(magician.title())


magician_names = ['jim', 'danny', 'guy', 'pal']
show_magicians(magician_names)
make_great(magician_names[:])
print(magician_names)


