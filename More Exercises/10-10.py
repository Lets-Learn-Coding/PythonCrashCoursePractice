#common words
filename = 'book.txt'
with open(filename) as f_obj:
    words = f_obj.read()
    print (words)
    print (words.lower().count('the'))
