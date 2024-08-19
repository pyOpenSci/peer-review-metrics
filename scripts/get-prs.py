"""A script that parses all active pyos repos and collects contributor and 
activity information in the form of opened issues and pull requests. 

This script returns a .csv file that contains all issue and pr data for items:

* not created by a bot 
* and created in the specific current year.

The one issue with this workflow is that if it doesn't run on the last day of 
the year, then it won't capture the last pr's that might happen on new years 
eve week. 

This will allow us to track contribution growth overtime. 

Ideally this should be run as a cron job, a workflow dispatch and then 
on near years eve 

    # Run specifically on New Year's Eve at 11:30 PM
    - cron: '30 23 31 12 *'
     
That way we are sure to capture data for the entirety of 2024 on new years eve!!

"""

import logging
import os
import time
import datetime

import pandas as pd
from datetime import datetime

from pyosmeta.github_api import GitHubAPI

logging.basicConfig(level=logging.INFO)


def get_repo_data(
    github_api,
    repo_name,
    endpoint_type,
    contrib_types,
    user_location_cache: dict[str:str],
):
    """
    Get repository data from GitHub API and save it as a CSV file.

    Parameters
    ----------
    github_api : GitHubAPI
        An instance of the GitHubAPI class.
    repo_name : str
        The name of the repository.
    endpoint_type : str
        The type of endpoint to retrieve data from. Options (pull or issue)
    contrib_types : dict
        A dictionary containing contributor types.

    Returns
    -------
    DataFrame
        A pandas DataFrame containing the repository data.

    Raises
    ------
    None
    """

    github_api.endpoint_type = endpoint_type
    items = github_api.return_response()
    contrib_type = "contributor"

    data = []
    for item in items:
        gh_user = item["user"]["login"]
        if gh_user in contrib_types["bots"]:
            continue  # Skip items created by bots
        elif gh_user in contrib_types["pyos_staff"]:
            contrib_type = "staff"  # Flag items that are core staff

        created_at = datetime.strptime(
            item["created_at"], "%Y-%m-%dT%H:%M:%SZ"
        )
        labels = [label["name"] for label in item.get("labels", [])]

        # TODO: make this a small function
        if gh_user in user_location_cache:
            location = user_location_cache[gh_user]
        else:
            location = github_api.get_user_info(gh_handle=gh_user).get(
                "location", ""
            )
            user_location_cache[gh_user] = location
        data.append(
            {
                "title": item["title"],
                "item_opened_by": created_at,
                "current_status": item["state"],
                "labels": ", ".join(labels),
                "created_by": gh_user,
                "location": location,
                "contrib_type": contrib_type,
                "repo": repo_name,
                "type": endpoint_type,
            }
        )

    return pd.DataFrame(data)


def process_repo(github_api, repo_name, contrib_types, user_location_cache):
    """Process a GitHub repository.

    Export a repo_name.csv file for the repo when done.

    Parameters
    ----------
    github_api : object
        The GitHub API object.
    repo_name : str
        The name of the repository to process.
    contrib_types : dict
        A dict containing sublists of pyOS staff members & then bots
        that contribute to pyos repos.
    user_location_cache : dict
        A dictionary containing the cached user locations.

    Returns
    -------
    dict
        A dictionary containing the processed issues and pull requests of the repository.

    Raises
    ------
    Exception
        If an error occurs during the processing.
    """

    github_api.repo = repo_name
    try:
        print(f" -- Getting issues for {repo_name}")
        issues_df = get_repo_data(
            github_api, repo_name, "issues", contrib_types, user_location_cache
        )
        print(f" -- Getting prs for {repo_name}")
        prs_df = get_repo_data(
            github_api, repo_name, "pulls", contrib_types, user_location_cache
        )
        print(f" -- Combining issues and prs for {repo_name}")
        all_contribs_df = pd.concat([issues_df, prs_df], ignore_index=True)
        # Remove items created before 2024 - this is a hack to account for the
        # rest
        all_contribs_df = all_contribs_df[
            all_contribs_df["item_opened_by"] >= "2024-01-01"
        ]
        print(f" -- Finished with {repo_name} API calls")

        return all_contribs_df
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def main():
    # Get the current year
    current_year = datetime.now().year
    after_date = f"{current_year}-01-01"

    github_api = GitHubAPI(
        org="pyopensci", repo="", endpoint_type="", after_date=after_date
    )

    contrib_types = {
        "pyos_staff": [
            "lwasser",
            "kierisi",
        ],
        "bots": [
            "allcontributors[bot]",
            "pre-commit-ci[bot]",
        ],
    }

    # Note: this should be stored somewhere centrally as we use this list
    # for the get contributors workflow as well.
    repo_names = [
        "python-package-guide",
        "software-peer-review",
        "pyosMeta",
        "pyopensci.github.io",
        "handbook",
        "software-submission",
        "peer-review-metrics",
        "pyosPackage",
        "pyos-sphinx-theme",
    ]
    all_contribs_final = []  # Create an empty DataFrame

    # Object to reduce user api calls.
    # The alternative is to retrieve contrib location data at the end
    user_location_cache = {}
    for repo_name in repo_names:
        start_time = time.time()
        print(f"Processing repository: {repo_name}")
        all_contribs_df = process_repo(
            github_api, repo_name, contrib_types, user_location_cache
        )

        print(f"Adding new df data for {repo_name} & saving csv")
        all_contribs_final.append(all_contribs_df)
        end_time = time.time()

        print(
            f"{repo_name}--Processing Time: {end_time - start_time:.4f} seconds"
        )

    all_contribs_final_df = pd.concat(all_contribs_final, ignore_index=True)

    # Write all_contribs_final_df to a single CSV file
    os.makedirs("_data", exist_ok=True)
    all_contribs_final_df.to_csv(
        os.path.join("_data", f"{current_year}_all_issues_prs.csv"),
        index=False,
    )


if __name__ == "__main__":
    main()