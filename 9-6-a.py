#Ice Cream Stand

class restaurant():
    #modeling a restaurant
    def __init__(self, name, cuisine, about, people):
        self.name = name.title()
        self.cuisine = cuisine
        self.about = about
        self.people = people

    def open_restaurant(self):
        print ('Welcome to ' + self.name.title() + '!')

    def food(self):
        print (self.name + ' has ' + self.cuisine + '!')

    def describe(self):
        print (self.about)

    def count(self):
        print ('Served ' + str(self.people))

    def add(self, person):
        self.people += person
        print (str(person) + " people walked in.")
        print ("Served " + str(self.people))

class icecream_stand(restaurant):
    def __init__(self, name, cuisine, about, people):
        super().__init__(name, cuisine, about, people)
        self.flavors = []
    def flavor_list(self, *flavors):
        for item in flavors:
            self.flavors.append(item)
        print (self.flavors)


ice = icecream_stand('andys', 'icecream', 'Cool place', 5)
ice.flavor_list('bbq', 'cheese')
