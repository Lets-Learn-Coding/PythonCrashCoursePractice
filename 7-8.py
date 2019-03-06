#deli
sandwich_orders = ['blt', 'burger', 'grilled cheese']
finished_sandwiches = []
while sandwich_orders:
    for item in sandwich_orders:
        print ('I made your ' + item + '!')
        finished_sandwiches.append(item)
        sandwich_orders.remove(item)
print (finished_sandwiches)
