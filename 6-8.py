#Pets

newman ={
    'name': 'newman',
    'type': 'cat',
    'owner': 'nic',
    'color': 'black'
}

rocky ={
    'name': 'rocky',
    'type': 'cat',
    'owner': '?',
    'color': 'brown'
}

maggie ={
    'name': 'maggie',
    'type': 'dog',
    'owner': 'nic',
    'color': 'yellow'
}

scarlett ={
    'name': 'scarlett',
    'type': 'dog',
    'owner': 'allie',
    'color': 'white and brown'
}

pets = [newman, rocky, maggie, scarlett]

for pet in pets:
        print (pet['name'].title() + ' is a ' + pet['color'] + " " + pet['type'] + ' and they belong to ' + pet['owner'].title() + ".")
