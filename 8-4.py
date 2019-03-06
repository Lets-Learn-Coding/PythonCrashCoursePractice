#large shirts
size = input('Enter a size SM M LG: ').upper()

def make_shirt(size):
    if size != 'SM' and size != 'M' and size != 'LG':
        print ('Size not available, try again.')
        size = input('Enter a size SM M LG: ').upper()
        make_shirt(size)

    if size == 'M' or size == 'LG':
        print ('You have a ' + size + ' shirt that says - I love Python! -')
    else:
        text = input('Enter your text for your shirt: ')
        print ('You have a ' + size + ' shirt that says - ' + text + ' -')

make_shirt(size)