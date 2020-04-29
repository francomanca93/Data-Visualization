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
repo_links, stars, labels = [], [], []  # Lists to show the repositories names, stars and labels
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)  # Append repository link and name
    
    stars.append(repo_dict['stargazers_count']) # Append star of the repositories

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"  # Plotly allows you to use HTML code within text elements. Label is a string with a line break (<br />)
    labels.append(label)  # Append label (owner and description) to labels


# Make visualization. Changes to the 'data' object affect the bars visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker':{  # The marker settings affect the design of the bars
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size':28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size':24},
        'tickfont': {'size':14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size':24},
        'tickfont': {'size':14},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
