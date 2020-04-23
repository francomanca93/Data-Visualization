import json

from plotly.graph_objs import Scattergeo, Layout  # Scattergeo allow you plot of geographic data on a map. Layout is a class
from plotly import offline  # offline module allow you to render a map

# Explore the structure of the data.
filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # store entire set of data

# store all dictionaries
all_eq_dicts = all_eq_data['features']  # I took the data associated with the key 'features' and store

# extracting magnitudes, longitudes, latitudes from the json data
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # I stored the magnitudes data that it is conteined in 'properties' dictionary
    lon = eq_dict['geometry']['coordinates'][0] # I stored the longiteds data that it is conteined in 'geometry'--> 'coordinates'
    lat = eq_dict['geometry']['coordinates'][1] # I stored the latitudes data that it is conteined in 'geometry' --> 'coordinates'
    mags.append(mag)  # Append the mag data
    lons.append(lon) # Append the longitudes data
    lats.append(lat) # Append the latitudes data

# Map the eathquakes.
data = [{  # I created the Scattergeo object inside the list data. Inside the list the data is structured as key-value pairs.
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        },
}]
my_layout = Layout(title='Global Earthquakes')  # I instance from a Layout class that it is conteined in plotly.graph_objs

fig = {'data': data, 'layout': my_layout}  # Dictionary that conteins the data and the layout.
offline.plot(fig,filename='global_earthquakes.html')  # With offline.plot() function I can plot the data


