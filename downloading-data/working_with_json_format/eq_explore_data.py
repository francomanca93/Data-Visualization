import json

# Explore the structure of the data.
filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # store entire set of data

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

