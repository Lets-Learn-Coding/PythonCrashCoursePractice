#Cities
def describe_city(city, country):
    print(city.title()  + ' is in ' + country.title() + '.')

city = input('Enter a city: ')
country = input('Enter a country: ')

describe_city(city, country)