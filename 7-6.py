#Three Exits
foods= {
    'banana':{
        'color': 'yellow',
        'type': 'fruit'
    },
    'pizza': {
        'color': 'orange',
        'type': 'carbs'
    },
    'egg_roll': {
        'color': 'brown',
        'type': 'chinese'
    }
}

for food, info in foods.items():
    print (food)
    print(info['color'])

