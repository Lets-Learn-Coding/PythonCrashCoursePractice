# Sandwiches
def sandwich(meat, *toppings):
    sandwich = meat.title() +' sandwich'
    print ('You ordered a ' + sandwich  + '!\n' )
    print ('Your ' + sandwich + ' is topped with:' + '\n')
    for topping in toppings:
        print ('- ' + topping)

sandwich('turkey', 'egg', 'pizza', 'cheese')

#try making this function using user inputs
