# Restaurant Seating
people = input('Table for how many people: ')

if int(people) > 8:
    print ("Sorry, you'll have to wait.")
else:
    print ("Excellent! Table for " + people + " coming right up!")