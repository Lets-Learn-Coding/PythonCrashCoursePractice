#10-5 Prog poll
filename =  'prog_poll.txt'

def question():
    while True:
        q_one = input('Why do you like programming?: ')
        with open(filename, 'w') as file_object:
            file_object.write(q_one + '\n')
        more = input('Enter more reasons? Y/N: ')
        if more.upper() == 'Y':
            more = ''
            add()
            break
        else:
            break



def add():
    while True:
        q_one = input('Why do you like programming?: ')
        with open(filename, 'a') as file_object:
            file_object.write(q_one + '\n')
        more = input('Enter more reasons? Y/N: ')
        if more.upper() == 'Y':
            True
        else:
            break

def full():
    which = input('-new- file or -add- to old file?: ')
    if which == 'add':
        print ('Adding these to ' + filename)
        add()
    elif which == 'new':
        print ('Making ' + filename + ' a new file.')
        question()
    else:
        full()




full()





