#10-4 Guestbook program

filename = 'guest_book.txt'
times = int(input('How many names do you want to enter (number): '))


while True:
    while times > 0:
        name = input('Enter a name for the guest book: ')
        with open(filename, 'a') as file_object:
            file_object.write(name + ('\n'))
        times -= 1
        if times == 0:
            print ('Done adding')
            break

