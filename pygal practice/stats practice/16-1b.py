#get mean from death valley
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename ='death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    means, dates = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            mean = int(row[2])
        except ValueError:
            print(current_date, 'missing mean')
        else:
            means.append(mean)
            dates.append(current_date)

#plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, means, c='blue')
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temp(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()