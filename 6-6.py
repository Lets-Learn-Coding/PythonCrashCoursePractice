#people

persons = {
    'Anthony': {
        'color': 'purple',
        'music': 'psychedelic',
        'drink': 'absinthe'
    },
    'Tommy': {
        'color': 'blue',
        'music': 'blink 182',
        'drink': 'beer'
    },
    "Nic": {
        'color': 'green',
        'music': 'rock',
        'drink': 'coffee'    }
}

for person, name in persons.items():
    print (person + "'s favorite color is " + name['color'] + "!")
    print (person + "'s favorite music is " + name['music'] + ' and their favorite drink is ' + name['drink'] + '!')