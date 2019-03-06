# User

class user():
    def __init__(self, first_name, last_name):
        user.first = first_name
        user.last = last_name


    def describe(self):
        print ('First name is: ' + user.first.title() + ('\n') + 'Last name is: ' + user.last.title())

    def greet(self):
        name = (user.first.title() + ' ' + user.last.title())
        print ('Welcome ' + name + '!')

me = user('nic', 'mazil')
me.describe()
me.greet()
person = user(input('Enter first name: '), input('Enter last name:'))
person.greet()
person.describe()