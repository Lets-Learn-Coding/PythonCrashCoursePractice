#Login Attempts

class user():

    def __init__(self, first_name, last_name):
        user.first = first_name
        user.last = last_name



    def describe(self):
        print ('First name is: ' + user.first.title() + ('\n') + 'Last name is: ' + user.last.title())

    def greet(self):
        name = (user.first.title() + ' ' + user.last.title())
        print ('Welcome ' + name + '!')

    def logins(self,login):
        login += 1
        print(str(login) + ' Attempts')

    def reset(self):
        login = 0
        print ('Resetting logins....')
        print(str(login) + ' Attempts')

me = user('nic', 'mazil')
me.describe()
me.greet()
me.logins(1)
me.reset()

person = user(input('Enter first name: '), input('Enter last name:'))
person.greet()
person.describe()
person.logins(2)
person.reset()