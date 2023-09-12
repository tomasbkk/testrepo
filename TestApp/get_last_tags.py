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

# Function to get the date from a tag object
def get_tag_date(tag):
    try:
        # Try to get the tagger date, and if it's not available, use the committer date
        return tag['commit']['tagger']['date']
    except KeyError:
        try:
            return tag['commit']['committer']['date']
        except KeyError:
            return ""

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    tags = response.json()

    # Sort tags by their creation date (using the get_tag_date function)
    sorted_tags = sorted(tags, key=get_tag_date, reverse=True)

    # Get the last 2 tags (the most recent ones)
    last_two_tags = sorted_tags[:2]

    # Print the names of the last two tags
    for tag in last_two_tags:
        print("Tag Name:", tag["name"])

# Set GitHub environment variables for the last two tags
if last_two_tags:
    os.environ["LAST_TAG"] = last_two_tags[0]["name"]
    os.environ["SECOND_LAST_TAG"] = last_two_tags[1]["name"]
else:
    print("Failed to fetch tags. Status code:", response.status_code)
