import json

# Explore the structure of the data.
filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # store entire set of data

# store all dictionaries
all_eq_dicts = all_eq_data['features']  # I took the data associated with the key 'features' and store

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # I stored the mag data that it is conteined in 'properties' dictionary
    mags.append(mag)  # Append the mag data

print(mags[:10])  # Print the 10 first mag
print(mags)

