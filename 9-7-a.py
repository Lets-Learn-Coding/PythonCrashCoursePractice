#Admin

# User

class user():
    def __init__(self, first_name, last_name):
        self.first = first_name.title()
        self.last = last_name.title()


    def describe(self):
        print ('First name is: ' + self.first.title() + ('\n') + 'Last name is: ' + self.last.title())

    def greet(self):
        name = (user.first.title() + ' ' + user.last.title())
        print ('Welcome ' + name + '!')

class admin(user):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name,)
        self.privel = privel()

class privel():
    def __init__(self):
        self.priv = ['can edit', 'can delete']
    def desc(self):
        print ('Permissions include:')
        print (self.priv)







me = admin('nic', 'mazil')
me.describe()
me.privel.desc()