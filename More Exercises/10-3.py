#guest exercise
filename = 'guest.txt'
name = input('Enter your name: ')

with open(filename, 'w') as file_object:
    file_object.write(name)

with open(filename) as file_object:
    print (file_object.read())


