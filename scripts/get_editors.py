"""This script parses a largely manually created list of editors 
grabbed from our onboarding form. It then merges this data with the editorial 
board GitHub team grabbed using graphQL. 

This provides a table with github username and technical and scinece domain areas 
that we can use. 

I then pulled domains and gh_usernames to allow us to create a table with 
editors and associated domains

TODO:
* it would be good to find a more automated way to get the domain data from our 
google sheet. one way to do this would be to use the airtable api if we move to airtable.
"""

import os

import requests
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

load_dotenv()

# Replace with your GitHub personal access token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/graphql"


def get_team_members():
    query = """
    {
      organization(login: "pyOpenSci") {
        team(slug: "editorial-board") {
          members(first: 100) {
            nodes {
              login
            }
          }
        }
      }
    }
    """

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.post(
        GITHUB_API_URL, json={"query": query}, headers=headers
    )

    if response.status_code == 200:
        data = response.json()
        members = data["data"]["organization"]["team"]["members"]["nodes"]
        return [member["login"] for member in members]
    else:
        print(f"Failed to retrieve team members: {response.status_code}")
        print(response.text)
        return []


def filter_members(members, exclude):
    return [member for member in members if member not in exclude]


if __name__ == "__main__":
    members = get_team_members()
    exclude = [
        "lwasser",
        "chayadecacao",
        "xuanxu",
    ]
    editorial_team_gh = filter_members(members, exclude)

    data_dir = Path("_data")
    editor_domains = pd.read_csv(data_dir / "editor-domains.csv")
    editor_domains["gh_username"] = editor_domains["gh_username"].str.replace(
        "@", ""
    )

    if editorial_team_gh:
        editorial_team_df = pd.DataFrame(
            editorial_team_gh, columns=["gh_username"]
        )

all_editors = pd.merge(
    editorial_team_df, editor_domains, on="gh_username", how="outer"
)

output_file = data_dir / "editorial_team_domains.csv"
all_editors.to_csv(output_file, index=False)
