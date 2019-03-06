#admin
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
class admin(user):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.perm = ['can delete', 'can post', 'can edit']

    def show_perm(self):
        print (str(self.perm))

class priv(privl):
    super().__init__()
    def show_perm(self):
        print (str(self.perm))

me = admin('Nic', 'Mazil')
me.show_perm()