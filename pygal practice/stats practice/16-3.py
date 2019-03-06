#16-3 Rainfall
#Check the rainfall for one month then do it for a full year of data

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    rains, date = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')

            rain = int(row[1])
        except ValueError:
            print(current_date, 'missing rain')
        else:
            rains.append(rain)
            date.append(current_date)

#plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(date, rains, c='blue')
#format plot
plt.title('Rainfall in Sitka for the Year', fontsize=24)
plt.ylabel('Rain', fontsize=16)
plt.xlabel("", fontsize=16)


plt.show()
