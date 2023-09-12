import os
import requests
import json

# GitHub repository information
owner = "tomasbkk"
repo = "testrepo"

# GitHub GraphQL API endpoint
api_url = "https://api.github.com/graphql"

# GitHub Personal Access Token (replace with your token)
access_token = "YOUR_ACCESS_TOKEN"

# GraphQL query to fetch the last two tags
query = """
{
  repository(owner: "%s", name: "%s") {
    refs(refPrefix: "refs/tags/", last: 2) {
      edges {
        node {
          name
          target {
            ... on Tag {
              tagger {
                date
              }
            }
          }
        }
      }
    }
  }
}
""" % (owner, repo)

headers = {
    "Authorization": f"Bearer {access_token}"
}

# Make a POST request to the GraphQL API
response = requests.post(api_url, json={"query": query}, headers=headers)

# Initialize variables to store the last two tags
last_two_tags = []

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    tags = data.get("data", {}).get("repository", {}).get("refs", {}).get("edges", [])

    # Extract tag names and tagger dates
    tag_info = [(tag["node"]["name"], tag["node"]["target"]["tagger"]["date"]) for tag in tags]

    # Sort tags by their tagger dates
    sorted_tags = sorted(tag_info, key=lambda x: x[1], reverse=True)

    # Get the last 2 tags (the most recent ones)
    last_two_tags = sorted_tags[:2]

    # Print the names of the last two tags
    for tag_name, _ in last_two_tags:
        print("Tag Name:", tag_name)

# Set GitHub environment variables for the last two tags
if last_two_tags:
    os.environ["LAST_TAG"] = last_two_tags[0][0]
    os.environ["SECOND_LAST_TAG"] = last_two_tags[1][0]
else:
    print("Failed to fetch tags. Status code:", response.status_code)
