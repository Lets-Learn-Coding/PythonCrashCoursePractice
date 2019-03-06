#persson

person = {
    'first_name': "nic",
    'last_name': 'mazil',
    'age': 24,
    'city': 'brookfield'
}

print (person['first_name'].title() + " is the person's first name!")
print (person['last_name'].title() + " is the person's last name!")
print (person['first_name'].title() + " " + person['last_name'].title() + " is the person's full name!")
full = (person['first_name'].title() + " " + person['last_name'].title())
print (full)
print (full + "'s" + " age is " + str(person['age']))
print (full + "'s" + ' city is ' + person['city'].title())

favnum = {
    'nic': 7,
    'tom': 2,
    'fred': 3,
}
print ("Nic's favorite number is " + str(favnum['nic']))

for key, value in favnum.items():
    print ("Name: " + key.title() + " Favorite Number: " + str(value))