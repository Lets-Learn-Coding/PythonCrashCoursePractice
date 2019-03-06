# compressing the user function even more

import json

def get_stored():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def new_username():
    username = input('What is your name: ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet():
    username = get_stored()
    if username:
        print ("welcome back " + username + '!')
    else:
        username = new_username()
        print ("We'll remember you " + username +  "!")

greet()