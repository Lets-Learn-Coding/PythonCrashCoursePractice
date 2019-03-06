# filenotfound error exception

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + ' does not exist.'
        print (msg)
    else:
        words = contents.split()
        num = len(words)
        print ("The file " + filename + " has about " +  str(num) + " words.")

filename = 'alice.txt'
count_words(filename)
