# Favorite number program

import json

#looks for the stored favorite number by looking at fav.json

def stored():
    filename = 'fav.json'
    try:
        with open(filename) as f_obj:
            fav = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav

def new_fav():
    filename = 'fav.json'
    fav = input('Enter your favorite number: ')
    with open(filename, 'w') as f_obj:
        json.dump(fav, f_obj)
    return fav

def num():
    fav = stored()
    if fav:
        print ('I remembered that your favorite number is ' + str(fav) + '!')
    else:
        fav = new_fav()
        print ("I'll remember that your fav number is " + str(fav) + "!")

num()