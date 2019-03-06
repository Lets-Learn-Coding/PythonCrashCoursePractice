#Cars
def build_car(manufacturer, model, **extras):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in extras.items():
        car[key] = value
    return car

my_car = build_car('nissan', 'altima', year= 2016, insurance= 'yes')
print (my_car)