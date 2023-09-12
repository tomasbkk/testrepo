import os
import requests

# GitHub repository information
owner = "tomasbkk"
repo = "testrepo"

# GitHub API endpoint to list tags
api_url = f"https://api.github.com/repos/{owner}/{repo}/tags"

# Make a GET request to the API
response = requests.get(api_url)

# Initialize variables to store the last two tags
last_two_tags = []

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response and sort tags by name
    tags = response.json()
    tags.sort(key=lambda tag: tag["name"])

    # Get the last 2 tags (the most recent ones)
    last_two_tags = tags[-2:]

    print("Tags:")
    for tag in tags:
        print("Tag Name:", tag["name"])

# Set GitHub environment variables for the last two tags
if last_two_tags:
    os.environ["LAST_TAG"] = last_two_tags[1]["name"]
    os.environ["SECOND_LAST_TAG"] = last_two_tags[0]["name"]
else:
    print("Failed to fetch tags. Status code:", response.status_code)
