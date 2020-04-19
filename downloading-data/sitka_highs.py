import csv

import matplotlib.pyplot as plt

filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/data/sitka_weather_07-2018_simple.csv'
# filename = 'data/sitka_weather_07-2018_simple.csv'  # String object

with open(filename) as f:  # Open the file and assign the resulting file object to 'f'
    reader = csv.reader(f)  # From csv I call the static method reader() and pass it a file object to create a reader object
    header_row = next(reader)  # the next function receive a reader object a get the firs line of the file.
    
    # Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)

# Plot the high temperatures.
plt.style.use('seaborn')
fig = plt.subplot()
ax = plt.subplot()
ax.plot(highs, c='red')

# Format plot
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('Days', fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
