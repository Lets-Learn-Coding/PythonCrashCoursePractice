import pygal
from die import Die

#make some die
die_1 = Die(6)
die_2 = Die(6)

#results of rolling dice 1000 times and multiplying results
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result =  die_1.num_sides * die_2.num_sides

for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize
hist = pygal.Bar()

hist.title = 'results of rolling 2 D6 and multiplying the rolls'

hist.x_labels = []
for num in range(1, max_result+1):
    hist.x_labels.append(num)

hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6 * D6', frequencies)
hist.render_to_file('15-9.svg')

