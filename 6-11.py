#Cities
cities ={
    "boulder": {
        'country': 'USA',
        'population': '100',
        'fact': 'Is in Colorado',
    },
    "chicago": {
        'country': 'Chiraq',
        'population': '2',
        'fact': 'It really sucks.',
    },
    "new york": {
        'country': 'USA',
        'population': '20',
        'fact': 'The big apple',
    }

}
for city, city_info in cities.items():
    print (city)
    print (city_info['country'])
    print ('Population: ' + city_info['population'])
    print ("Fun fact: " + city_info['fact'] +'\n')