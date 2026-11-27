#!/usr/bin/python3
"""Lists the 10 latest commits of a GitHub repository"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    commits = requests.get(url).json()
    for c in commits[:10]:
        name = c.get("commit").get("author").get("name")
        print("{}: {}".format(c.get("sha"), name))
