import requests

# GitHub repository information
owner = "tomasbkk"
repo = "testrepo"

# GitHub API endpoint to list tags
api_url = f"https://api.github.com/repos/{owner}/{repo}/tags"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    tags = response.json()

    # Get the last 2 tags (which are the most recent ones)
    last_two_tags = tags[-2:]

    # Print the last 2 tags
    for tag in last_two_tags:
        print("Tag Name:", tag["name"])
        print("Commit SHA:", tag["commit"]["sha"])
        print("--------")
else:
    print("Failed to fetch tags. Status code:", response.status_code)
