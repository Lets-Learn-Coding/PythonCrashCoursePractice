def city_name(city, country, population=''):
    if population == '':
        name = city.title() + ', ' + country.title() + population
    elif population != '':
        name = city.title() + ', ' + country.title() + ' - population ' + str(population)
    print (name)

city_name('brookfield', 'usa')
