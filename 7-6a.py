#Three Exits
word = ''
while word == '':
    word = input('Enter a word: ')
    print("The end!")

x = int(input("Enter a number: "))
while int(x) < 10:
    print (x)
    x += 1

word2 = ''
while word2 != 'quit':
    word2 = input('Enter Something: ')
    if word2 != 'quit':
        print(word2)
    else:
        break