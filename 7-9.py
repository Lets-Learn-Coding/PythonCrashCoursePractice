#No pastrami
sandwich = ['pastrami', 'blt', 'pastrami', 'grilled cheese']
done = []
while sandwich:
    for item in sandwich:
        if item == 'pastrami':
            sandwich.remove(item)
        else:
            print ('Here is a ' + item)
            done.append(item)
            sandwich.remove(item)
