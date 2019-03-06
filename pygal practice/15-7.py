#Two D8s
#Create a sim showing what happens if you roll 2 8 sided dice 1000 times

import pygal
from die import Die

#create two 8 sided dice
die_1 = Die(8)
die_2 = Die(8)

#make some rolls and store the results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D8 1000 times"
hist.x_labels = []
for x in range(2,17):
    hist.x_labels.append(x)
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file('15-7.svg')