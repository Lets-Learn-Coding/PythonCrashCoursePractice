# writes in the txt file
# sets the filename for easy access

filename = 'program.txt'

#with /open uses 2 arguments filename and 'w' to open the file in write mode
#Opens the file and the writes fuck this shit.

with open(filename, 'w') as file_object:
    file_object.write('Hello. \n')
    file_object.write("What's up? \n")

with open(filename) as file_object:
    print (file_object.read())

with open(filename, 'a') as file_object:
    file_object.write('Yo.')