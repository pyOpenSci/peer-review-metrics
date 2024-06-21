---
title: pyOpenSci stats
subtitle: Cause we like it like that
author:
  - name: Leah Wasser
    affiliations: pyOpenSci
    orcid: 0000-0002-7859-8394
    email: leah@pyopensci.org
license:
  code: MIT
date: 2024/06/20
---

# hello there 


:::{code-cell} python

from datetime import datetime

import altair as alt
import pandas as pd

from pyosmeta import ProcessIssues
from pyosmeta.github_api import GitHubAPI


def parse_single_issue(issue) -> dict:
    """
    Parse a single issue from the GitHub API response.

    Parameters
    ----------
    issue : dict
        Dictionary containing information about a single issue.

    Returns
    -------
    dict
        Dictionary containing parsed information about the issue.
    """
    parsed_issue = {}

    # Extract labels
    parsed_issue["labels"] = [label["name"] for label in issue.get("labels", [])]

    # Extract header text (title of the issue)
    parsed_issue["header_text"] = issue.get("title", "")

    # Extract date opened
    parsed_issue["date_opened"] = datetime.strptime(
        issue.get("created_at"), "%Y-%m-%dT%H:%M:%SZ"
    )

    # Extract date closed (if available)
    if issue.get("closed_at"):
        parsed_issue["date_closed"] = datetime.strptime(
            issue.get("closed_at"), "%Y-%m-%dT%H:%M:%SZ"
        )
        # Calculate total time issue was open
        time_open = parsed_issue["date_closed"] - parsed_issue["date_opened"]
        parsed_issue["time_open_days"] = time_open.total_seconds() / (60 * 60 * 24)
    else:
        parsed_issue["date_closed"] = None
        parsed_issue["time_open_days"] = None

    return parsed_issue

:::