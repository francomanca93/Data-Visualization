import json

# Explore the structure of the data.
filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # store entire set of data

# store all dictionaries
all_eq_dicts = all_eq_data['features']  # I took the data associated with the key 'features' and store

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # I stored the magnitudes data that it is conteined in 'properties' dictionary
    lon = eq_dict['geometry']['coordinates'][0] # I stored the longiteds data that it is conteined in 'geometry'--> 'coordinates'
    lat = eq_dict['geometry']['coordinates'][1] # I stored the latitudes data that it is conteined in 'geometry' --> 'coordinates'
    mags.append(mag)  # Append the mag data
    lons.append(lon) # Append the longitudes data
    lats.append(lat) # Append the latitudes data

print(mags[:10])  # Print the 10 first mag
print(lons[:5]) # Print the 5 first longitudes
print(lats[:5]) # Print the 5 first latitudes




