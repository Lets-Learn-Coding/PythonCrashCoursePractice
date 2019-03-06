#Magicians
magicians = ['Bob', 'magic mike', 'abracadabra']
over = []

def show_magicians(names):
    while magicians:
        for magician in names:
            print (magician.title() + ' is a magician!')
        break



show_magicians(magicians)