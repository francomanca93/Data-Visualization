import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # storing URL from API
headers = {'Accept':'application/vnd.github.v3+json'}  # Defining headers for the API call that ask explicity to use 3th version
r = requests.get(url,headers=headers)  # From 'requests' class, I use .get method to make call to the API
print(f"Status code: {r.status_code}")  # A status code of 200 indicates a successful response

# Store API response in a variable
response_dict = r.json()  # The API returns the information in JSON format, so we use the json() method to convert the information to a Python dictionary

# Process results.
print(response_dict.keys())
# Reposotories results
print(f"Total repositories (from total_count): {response_dict['total_count']}")  # the total number of Python repositories on GitHub.

# Explore information about the repositories.
repo_dicts = response_dict['items']  # The value associated with 'items' is a list of dictionaries
print(f"Repositories returned (from items): {len(repo_dicts)}")  # See how many repositories are 

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")  # Print the number of keys to see how much information we have.
for key in sorted(repo_dict.keys()):  # Print all the dictionary's keys to see what kind of information is included.
    print(key)


