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

