def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = 'the Great ' + magician
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['li', 'wu', 'qi']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)
