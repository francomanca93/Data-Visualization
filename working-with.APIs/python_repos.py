import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # storing URL from API
headers = {'Accept':'application/vnd.github.v3+json'}  # Defining headers for the API call that ask explicity to use 3th version
r = requests.get(url,headers=headers)  # From 'requests' class, I use .get method to make call to the API
print(f"Status code: {r.status_code}")  # A status code of 200 indicates a successful response

# Store API response in a variable
response_dict = r.json()  # The API returns the information in JSON format, so we use the json() method to convert the information to a Python dictionary

# Reposotories results
print(f"Total repositories (from total_count): {response_dict['total_count']}")  # the total number of Python repositories on GitHub.

# Explore information about the repositories.
repo_dicts = response_dict['items']  # The value associated with 'items' is a list of dictionaries
print(f"Repositories returned (from items): {len(repo_dicts)}")  # See how many repositories are 

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

# Monitoring API rate limits
# Most API are rate limited, which means there's a limit to how many requests you can make in a certain
# amount of time. To see if you're approaching GitHub's limits, enter https://api.github.com/rate_limit. 
# The information we’re interested in is the rate limit for the search API.
