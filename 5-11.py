#Ordinal Numbers
num = list(range(1,10))
print (num)
for number in num:
    if number == 1:
        print ('1st')
    elif number == 2:
        print ('2nd')
    elif number == 3:
        print ('3rd')
    elif number >= 4:
        print (str(number) + 'th')