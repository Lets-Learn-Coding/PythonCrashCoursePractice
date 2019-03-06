#UNchanged Magicians
#Great MAGICIANS

magicians = ['Bob', 'magic mike', 'abracadabra']
over = []

def show_magicians(list, empty):
    list2 = list[:]
    while list2:
        for magician in list2:
            print (magician.title() + ' is a magician!')
            empty.append('the Great ' + magician)
            list2.pop()





show_magicians(magicians, over)
print (magicians)
print (over)