from die import Die
import matplotlib.pyplot as plt

die_1 = Die(6)
die_2 = Die(6)

results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

label =[]
for x in range(2, max_result+1):
    label.append(x)


plt.plot(label, frequencies , linewidth =5)

#set chart title and label axes
plt.title("Results D6 + D6", fontsize=24)
plt.xlabel('D6 + D6', fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

#set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
