# Conditional Tests
car = 'subaru'

print ('Hmm, is this a subaru?')
if car == 'subaru':
    print ('\n I predict true!')

print ('\n Is this an audi?')
if car != 'audi':
    print ("\n That's not an audi.")

print('\n')

def number_picker():
    print ('Is your number greater than 2?')
    x = input('Enter an int!: ')
    print ('Is ' + str(x) + ' greater than 2?')
    x = int(x)
    if x > 2:
        print ('yup!')
    elif x == 2:
        print ("They're the same!")
    else:
        print ('nope')


number_picker()


word = 'TITLE'
if word.lower() == 'title':
    print ('Same!')