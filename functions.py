"""
A small module to store functions used to process data in this
repo

"""

from datetime import datetime


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
        parsed_issue["days_open"] = time_open.total_seconds() / (60 * 60 * 24)
    else:
        parsed_issue["date_closed"] = None
        # calculate time delta
        delta = datetime.now() - parsed_issue["date_opened"]
        parsed_issue["days_open"] = delta.days

    return parsed_issue


def count_edits_by_quarter(df):
    """
    Count submission edited by each editor by quarter.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe containing a ``created_at`` datetime column and
        an ``editor`` column.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the number of submissions edited by each editor
        by quarter.
    """
    n_edits = df.groupby(by=[df["editor"], df["created_at"].dt.to_period("Q")]).count()
    n_edits.rename(columns=dict(created_at="n_edits"), inplace=True)
    return n_edits


def test_count_edits_by_quarter():
    import pandas as pd

    # Build a sample df
    sample_df = pd.DataFrame(
        {
            "created_at": [
                "2024-03-01",
                "2024-06-18",
                "2024-11-12",
                "2024-12-12",
                "2024-03-11",
                "2024-04-12",
            ],
            "editor": ["foo", "foo", "foo", "foo", "bar", "bar"],
        }
    )
    sample_df["created_at"] = pd.to_datetime(sample_df.created_at)

    # Get n_edits with the function
    n_edits = count_edits_by_quarter(sample_df)

    # Build expected df
    expected = pd.DataFrame(
        {
            "n_edits": {
                ("bar", pd.Period("2024Q1", "Q-DEC")): 1,
                ("bar", pd.Period("2024Q2", "Q-DEC")): 1,
                ("foo", pd.Period("2024Q1", "Q-DEC")): 1,
                ("foo", pd.Period("2024Q2", "Q-DEC")): 1,
                ("foo", pd.Period("2024Q4", "Q-DEC")): 2,
            }
        }
    )
    expected.index.names = ["editor", "created_at"]

    # Test if output matches the expected one
    pd.testing.assert_frame_equal(expected, n_edits)