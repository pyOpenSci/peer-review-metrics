"""
    
# TODO it would be helpful to have pyosmeta return 
# * unique issue/pr identifier
# * who opened the issue (gh username of that person)


    _extended_summary_
"""

import os
from datetime import datetime

import pandas as pd

from pyosmeta import ProcessIssues
from pyosmeta.github_api import GitHubAPI

pd.options.mode.chained_assignment = None
pd.options.future.infer_string = True


def get_reviews(org, repo, labels):
    github_api = GitHubAPI(
        org=org,
        repo=repo,
        labels=labels,
    )
    process_review = ProcessIssues(github_api)
    issues = process_review.get_issues()
    reviews, errors = process_review.parse_issues(issues)
    return reviews


def process_submissions(submission_type, labels):
    reviews = get_reviews("pyopensci", "software-submission", labels)
    submission_table = [
        {
            "package_name": name,
            "date_opened": review.created_at,
            "date_closed": review.closed_at,
            "labels": review.labels,
            # "id": review.node_id,
            # "number": review.number,
        }
        for name, review in reviews.items()
    ]

    return pd.DataFrame(submission_table)


def set_review_status(labels, issue_map):

    highest_label = None
    highest_value = -1

    # Check for special conditions
    if "presubmission" in labels:
        return "presubmission"
    elif "currently-out-of-scope" in labels:
        return "out of scope"
    elif any(
        label in labels
        for label in ["⌛ pending-maintainer-response", "on-hold"]
    ):
        return "on hold"

    for i, label in enumerate(labels):
        if "/" not in label:
            continue

        value = int(label.split("/")[0])

        if value > highest_value:
            highest_label = labels[i]

    # If highest_label is set, map it; otherwise, default to 'pre-review'
    return issue_map.get(highest_label)


def main():
    submission_types = {
        "presubmission": ["presubmission"],
        "submission": [
            "0/seeking-editor",
            "0/pre-review-checks",
            "1/editor-assigned",
            "2/seeking-reviewers",
            "3/reviewers-assigned",
            "4/reviews-in-awaiting-changes",
            "5/awaiting-reviewer-response",
            "6/pyOS-approved",
            "7/under-joss-review",
            "8/joss-review-complete",
            "9/joss-approved",
            "New Submission!",
        ],
    }
    issue_map = {
        "New Submission!": "pre-review",
        "0/pre-review-checks": "pre-review",
        "0/seeking-editor": "seeking editor",
        "1/editor-assigned": "under-review",
        "2/seeking-reviewers": "under-review",
        "3/reviewers-assigned": "under-review",
        "4/reviews-in-awaiting-changes": "under-review",
        "5/awaiting-reviewer-response": "under-review",
        "6/pyOS-approved": "pyos-accepted",
        "9/joss-approved": "joss-accepted",
    }

    for submission_type, labels in submission_types.items():
        df = process_submissions(submission_type, labels)
        df["status"] = df["labels"].apply(set_review_status, args=(issue_map,))
        # Save csv file
        os.makedirs("_data", exist_ok=True)
        csv_path = os.path.join("_data", f"review_{submission_type}s.csv")
        df.to_csv(csv_path)
        print(f"{submission_type} processing done. Total: {len(df)}")


if __name__ == "__main__":
    main()
