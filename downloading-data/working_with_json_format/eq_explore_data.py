import json

from plotly.graph_objs import Scattergeo, Layout  # Scattergeo allow you plot of geographic data on a map. Layout is a class
from plotly import offline  # offline module allow you to render a map

# Explore the structure of the data.
filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_data_30_day_m1.json'
# filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_data_1_day_m1.json'
# filename = '/home/franco/Documents/Python/Proyectos/Data-Visualization/downloading-data/working_with_json_format/data/eq_7pm_hour_23-04-2020.json'

with open(filename) as f:
    all_eq_data = json.load(f)  # store entire set of data

# store all dictionaries
all_eq_dicts = all_eq_data['features']  # I took the data associated with the key 'features' and store

# extracting magnitudes, longitudes, latitudes from the json data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    # First go to the data that is conteined in properties o geometry and then to the data in specify.
    mags.append(eq_dict['properties']['mag'])  
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the eathquakes.
data = [{  # I created the Scattergeo object inside the list data. Inside the list the data is structured as key-value pairs.
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Hot',  # There are more colorscale like --> Bluered_r, Viridis, Inferno, Hot, etc...
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
        },
}]

title = all_eq_data['metadata']['title']
my_layout = Layout(title=title)  # I instance from a Layout class that it is conteined in plotly.graph_objs

fig = {'data': data, 'layout': my_layout}  # Dictionary that conteins the data and the layout.
offline.plot(fig,filename='global_earthquakes.html')  # With offline.plot() function I can plot the data


