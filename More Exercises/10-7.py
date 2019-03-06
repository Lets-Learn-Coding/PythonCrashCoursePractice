# 10-7 Addition Calc
def numbers():
    while True:
        first_number = input('Enter 1st number: ')
        second_number = input('Enter 2nd number: ')
        try:
            first_number = int(first_number)
            second_number = int(second_number)
        except ValueError:
            print('Only numbers')
        else:
            break
    print (first_number + second_number)

numbers()