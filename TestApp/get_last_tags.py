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

    # Extract tag names and create dates
    tag_dates = [(tag['name'], tag['commit']['author']['date']) for tag in tags]

    # Sort tags by their creation dates
    sorted_tags = sorted(tag_dates, key=lambda x: x[1])

    # Get the last 2 tags (the most recent ones)
    last_two_tags = sorted_tags[-2:]

    # Print the names of the last two tags
    for tag_name, _ in last_two_tags:
        print("Tag Name:", tag_name)

# Set GitHub environment variables for the last two tags
if last_two_tags:
    os.environ["LAST_TAG"] = last_two_tags[-1][0]
    os.environ["SECOND_LAST_TAG"] = last_two_tags[-2][0]
else:
    print("Failed to fetch tags. Status code:", response.status_code)
