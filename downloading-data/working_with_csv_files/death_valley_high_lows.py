import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_csv_files/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # convect date information to a datetime object
        # I use a block try/except/else because there are values in blank and appear the following error by console
        # ValueError: invalid literal for int() with base 10: ''
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)  # Append date
            highs.append(high)  # Append high temperature
            lows.append(low)  # Append low temperature

# Plot the high and low temperatures and its dates.
plt.style.use('seaborn')
fig = plt.subplot()
ax = plt.subplot()
ax.plot(dates, highs, c='red', alpha=0.5)  # I pass the dates and the high temperature values to plot()
ax.plot(dates, lows, c='blue', alpha=0.5)  # alpha controls a color's transparency
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

# Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)

plt.xlabel('Dates', fontsize=10)
plt.xticks(rotation=30)  # Rotate x ticks 30º

plt.ylabel("Temperature(F)", fontsize=10)

plt.tick_params(axis='both', which=None, labelsize=10)

plt.show()
