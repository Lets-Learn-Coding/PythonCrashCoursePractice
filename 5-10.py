#checking
current_users = ['cat', 'dog', 'fred', 'ted', 'tim']
new_users = ['cat', 'dog', 'nic', 'bill']

if new_users:
    for user in new_users:
        if user in current_users:
            print ('That name is used already!')
        else:
            print (user.title() + ' is available!')