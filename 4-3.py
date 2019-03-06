# range and lists
list2 = []
for i in range(1,21):
    list2.append(i)
print (list2)

# This is a list comprehension it does the same thing as the loop above but using less code
list = [number for number in range(1,21)]
print (list)

# List from one to 1k
thousand = [number for number in range(1, 1001)]
print (thousand)
for i in thousand:
    print (i)

mill = [number for number in range(1, 1000001)]

#smallest value in list
print (min(mill))

#max number in list
print (max(mill))

#sum of all numbers in list
print (sum(mill))

odds = [number for number in range(1, 21, 2)]
print (odds)

threes = [number*3 for number in range(3, 31)]
print (threes)

cubes = [number**3 for number in range(1,11)]
print (cubes)