# Script to create a readable json file from json file

import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()  # The API returns the information in JSON format, so we use the json() method to convert the information to a dictionary
readeble_file = '/home/franco/Documents/Python/Proyectos/Data-Visualization/working-with.APIs/data/readable_hn_data.json'
with open(readeble_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

