#List slicing
foods = ['apples', 'bananas', 'oranges', 'pears', 'pizza', 'ice cream']

print ('The first 3 foods are...')
print (foods[:3])

print ('The middle 3 foods are...')
print (foods[1:4])

print ('The last 3 items are..')
print (foods[3:])

pizzas = ['pepperoni', 'cheese', 'sausage', 'pineapple', 'deep dish']
friends_pizzas = pizzas[:]

print (friends_pizzas)
pizzas.append('jalapeno')
friends_pizzas.append('margarita')

print ('My favorite pizzas are....')
for pizza in pizzas:
    print (pizza)

print ('\n')
print ("My friend's favorite pizzas are..")
for pizza in friends_pizzas:
    print (pizza)