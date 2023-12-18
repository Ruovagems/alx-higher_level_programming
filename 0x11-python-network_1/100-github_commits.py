#!/usr/bin/python3
"""
This script lists 10 commits:
-(from the most recent to oldest);
-of a specified repository by a given user.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./list_commits.py <repository_name> <owner_name>")

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except ValueError:
        print("Not a valid JSON response from GitHub API")
