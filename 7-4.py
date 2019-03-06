#Pizza Toppings

topping = ""
prompt = "What would you like on your pizza: "

while True:
    print ('Enter a topping, or quit to exit.' + '\n')
    topping = input(prompt)





    if topping.lower() == 'quit':
        print ('Exiting....')
        break
    else:
        print('\n' + "I'll add " + topping + ' to your pizza!' + '\n')
        continue