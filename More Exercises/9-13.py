#OrderedDict Rewrite
#imports OrderedDict from collections
from collections import OrderedDict

#Makes a dictionary of items using the Ordereddict class
words = OrderedDict()

#stores a name and an item in a dictionary
words['Nic'] = 'python'
words['J'] = 'pizza'
#loops the dictionary
#for the key and string in the dictionary print the key likes string
for name, thing in words.items():
    print (name.title()  + ' likes ' + thing + ".")
