#Great MAGICIANS

magicians = ['Bob', 'magic mike', 'abracadabra']
over = []

def show_magicians(list, empty):
    while magicians:
        for magician in list:
            print (magician.title() + ' is a magician!')
            empty.append('the Great ' + magician)
            list.pop()





show_magicians(magicians, over)
print (magicians)
print (over)