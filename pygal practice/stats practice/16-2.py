#put sitka and death valley in one graph to compare high and low temps
from matplotlib import pyplot as plt
import csv
from datetime import datetime


#Get data from sitka
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[2]))


#Get data from death valley
filename2= 'death_valley_2014.csv'
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)

    highs2, dates2 = [], []
    for row in reader2:
        try:
            current_date2 = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
        except ValueError:
            print(current_date2, 'missing')
        else:
            dates2.append(current_date2)
            highs2.append(high)

#plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
#plot the highs from sitka as blue
plt.plot(dates, highs, c='blue')
#plot the highs from death valley as red
plt.plot(dates2, highs2, c ='red')

#format plot
plt.title('High Temps from Sitka and Death Valley', fontsize=24)
plt.ylabel('High Temp', fontsize=16)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.show()





