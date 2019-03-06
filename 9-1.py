#Restaurant Class
class restaurant():
    #modeling a restaurant
    def __init__(self, name, cuisine, about):
        self.name = name.title()
        self.cuisine = cuisine
        self.about = about

    def open_restaurant(self):
        print ('Welcome to ' + self.name.title() + '!')

    def food(self):
        print (self.name + ' has ' + self.cuisine + '!')

    def describe(self):
        print (self.about)



mine = restaurant('arbys', 'pizza', 'The biggest fast food chain!')
print (mine.name)
mine.open_restaurant()
mine.food()
mine.describe()