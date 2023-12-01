#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge.
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos\
/{}/{}/commits".format(owner, repo)
    res = requests.get(url)
    commits = res.json()
    latest_commit = commits[:10]
    for commit in latest_commit:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")

        print("{}: {}".format(sha, author))
