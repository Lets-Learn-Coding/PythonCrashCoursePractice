#Admin
users = ['matt', 'tim', 'admin', 'joe', 'nic']
if users:
    for name in users:
        if name == 'admin':
            print ('Hello ADMIN')
        else:
            print('Hello ' + name.title() + "!")
else:
    print ('Where are the users?')