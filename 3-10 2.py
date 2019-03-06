# This is a function that sorts in alphabetical/reverse alphabetical order
places = ['store', 'mountains', 'plains', 'beach', 'grassland']

def sortinghat(x):
    yn = input('Enter reg for alphabetical sorting, Enter rev for reverse alpha: ')
    yn = yn.lower()
    if yn == "reg" or yn == "rev":
        print ("Great!")
    else:
        print ("Invalid! Enter reg or rev!")
        return sortinghat(x)
    if yn == "reg":
        print ('Sorting in alphabetical order!')
        print (sorted(x))
        yesno = input('Sort again? Enter yes or y: ')
        yesno = yesno.lower()

        if yesno == "yes" or yesno == 'y':
            print ("Great!")
            return sortinghat(x)
        else:
            print ("Exiting...")
    elif yn == "rev":
        print ("Sorting in reverse")
        word = ('REVERSE')
        for i in word:
            print (i)
        x.sort()
        x.reverse()
        print (x)
        yesno = input('Sort again? Enter yes or y: ')
        yesno = yesno.lower()

        if yesno == "yes" or yesno == 'y':
            print ("Great!")
            return sortinghat(x)
        else:
            print ("Exiting...")



sortinghat(places)
print ("There are " + str(len(places)) + " places in the list!")