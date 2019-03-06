#get mean from sitka
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    mean, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        mean.append(row[2])

    print (mean)

#plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, mean, c='red')

#format plot
plt.title('Mean Temps', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temp(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()