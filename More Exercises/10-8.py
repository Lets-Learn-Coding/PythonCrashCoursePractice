#Cats and Dogs

with open('cats.txt', 'w') as f_obj:
    f_obj.write('hello \n')
    f_obj.write('djaoj \n')




def read(*filenames):
    for filename in filenames:
       try:
            with open(filename, encoding='utf-8') as f_obj:
                contents = f_obj.read()
                print (contents)
        except FileNotFoundError:
            pass

read('dogs.txt', 'cats.txt')