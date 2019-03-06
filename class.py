# Class
class dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print (self.name.title() + ' is now sitting.')

    def roll_over(self):
        print (self.name.title() + ' is rolling over.')

    def describe(self):
        print (self.name.title() + ' is ' + str(self.age) + '.')

dog('rover', 2).roll_over()
dog('jono', 3).sit()
dog('jooo', 3).describe()
my_dog = dog('maggie', 6)
print (my_dog.name.title())


class restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    def describe(self):
        print (self.name.title() + ' serves ' + self.cuisine + '.')
    def open(self):
        print(self.name.title() + ' is open!')
    def served(self):
        print(str(self.number_served) +  " people served.")
    def set_served(self, served):
        self.number_served += served
        print (str(self.number_served) + ' people served!')

restaurant('dogs', 'apples').describe()
restaurant('cats', 'fish').open()
my_rest = restaurant('Wendys', 'garbage')
my_rest.describe()
restaurant('booof', 'moo').served()
restaurant('boof', 'dogs').set_served(23)

class user():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login = 0
        self.name = self.first_name.title() + ' ' + self.last_name.title()
    def describe(self):
        print (self.first_name.title() + ' ' + self.last_name.title())
    def greet(self):
        print ('Hello ' + self.first_name.title() + ' ' + self.last_name.title() + '!')
    def login_attempts(self):
        self.login += 1
        print (str(self.login) + ' login attempts.')
    def reset_login(self):
        self.login = 0
        print ('Resetting login attempts....There are now ' + str(self.login) + ' attempts for user ' + self.name + '.')


my_user = user('Nic', 'Mazil')
my_user.greet()
my_user.describe()
my_user.login_attempts()
my_user.login_attempts()
my_user.login_attempts()
my_user.login_attempts()
my_user.reset_login()

