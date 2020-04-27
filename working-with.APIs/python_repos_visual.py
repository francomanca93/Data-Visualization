import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # storing URL from API
headers = {'Accept':'application/vnd.github.v3+json'}  # Defining headers for the API call that ask explicity to use 3th version
r = requests.get(url,headers=headers)  # From 'requests' class, I use .get method to make call to the API
print(f"Status code: {r.status_code}")  # A status code of 200 indicates a successful response

# Process results.
response_dict = r.json()  # The API returns the information in JSON format, so we use the json() method to convert the information to a Python dictionary
repo_dicts = response_dict['items']  # The value associated with 'items' is a list of dictionaries
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count']) 

# Make visualization. 
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
