#10-6 Addition

print ('Addition Program')
print ('Pick two numbers to add!')

first_number = (input('Enter a number: '))
try:
    first_number = int(first_number)
except ValueError:
    print ('input is not a number')

second_number = (input('Enter another number: '))
try:
    second_number = int(second_number)
except ValueError:
    print ('input is not a number')

print (first_number + second_number)

