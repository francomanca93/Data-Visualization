import json

# Explore the structure of the data.
filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # store entire set of data

readable_file = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)  # json.dump function takes JSON data object and a file object and write the data to that file
