import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/data/sitka_weather_2018_simple.csv'
# filename = 'data/sitka_weather_07-2018_simple.csv'  # String object

with open(filename) as f:  # Open the file and assign the resulting file object to 'f'
    reader = csv.reader(f)  # From csv I call the static method reader() and pass it a file object to create a reader object
    header_row = next(reader)  # the next function receive a reader object a get the firs line of the file.
    
    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # convect date information to a datetime object
        high = int(row[5])
        dates.append(current_date)  # Append date
        highs.append(high)  # Append high temperature


# Plot the high temperatures and its dates.
plt.style.use('seaborn')
fig = plt.subplot()
ax = plt.subplot()
ax.plot(dates, highs, c='red')  # I pass the dates and the high temperature values to plot()

# Format plot
plt.title("Daily high temperatures - 2018", fontsize=24)

plt.xlabel('Dates', fontsize=10)
plt.xticks(rotation=30)  # Rotate x ticks 30º

plt.ylabel("Temperature(F)", fontsize=10)

plt.tick_params(axis='both', which=None, labelsize=10)

plt.show()
