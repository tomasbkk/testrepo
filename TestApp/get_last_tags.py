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
    # Parse the JSON response
    tags = response.json()

    # Sort tags by their creation date (tagger -> date or commit -> committer -> date)
    sorted_tags = sorted(tags, key=lambda x: x['commit'].get('tagger', x['commit']['committer'])['date'], reverse=True)

    # Get the last 2 tags (the most recent ones)
    last_two_tags = sorted_tags[:2]

# Set GitHub environment variables for the last two tags
if last_two_tags:
    os.environ["LAST_TAG"] = last_two_tags[0]["name"]
    os.environ["SECOND_LAST_TAG"] = last_two_tags[1]["name"]
    print("Tag Name 1:", last_two_tags[0]["name"])
    print("Tag Name 2:", last_two_tags[1]["name"])
else:
    print("Failed to fetch tags. Status code:", response.status_code)
    
