# life stages!
age = input('Enter an age int: ')
age = int(age)
if age < 2:
    print ('Baby child')
elif age < 4:
    print ('toddler')
elif age < 13:
    print ('kiddo')
elif age < 20:
    print ('teen')
elif age < 65:
    print ('adult')
elif age >= 65:
    print ('elder')