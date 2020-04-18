import csv

# filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/data/sitka_weather_07-2018_simple.csv'

filename = 'data/sitka_weather_07-2018_simple.csv'  # String object
with open(filename) as f:  # Open the file and assign the resulting file object to 'f'
    reader = csv.reader(f)  # From csv I call the static method reader() and pass it a file object to create a reader object
    header_row = next(reader)  # the next function receive a reader object a get the firs line of the file.
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)


