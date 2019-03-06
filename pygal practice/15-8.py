import pygal
from die import Die


die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

#make some rolls and store the results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize results
hist = pygal.Bar()

hist.title = "Results of rolling 3 D6"
hist.x_labels = []
for x in range(3,19):
    hist.x_labels.append(x)
hist.x_title = "Result"
hist.y_title = 'Frequency of Results'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('15-8.svg')