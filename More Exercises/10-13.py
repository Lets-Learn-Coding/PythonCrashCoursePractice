#verify user

import json

def stored():
    filename = 'user.json'
    try:
        with open(filename) as f_obj:
            user = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user

def new_user():
    filename = 'user.json'
    user = input('Enter your name: ')
    with open(filename, 'w') as file_obj:
        json.dump(user, file_obj)
    print ("We'll remember you " + user + '!')
    return user

def greet():
    filename = 'user.json'
    user = stored()
    if user:
        print ('Your name is ' + user + '!')
        yn = input('Is this name correct y/n: ')
        if yn.upper() == 'Y':
            print ('Welcome ' + user + "!")
        else:
            print ('Enter the correct username.')
            new_user()
    else:
        new_user()

greet()