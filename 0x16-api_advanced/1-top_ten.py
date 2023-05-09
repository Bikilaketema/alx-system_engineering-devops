#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot
    posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json".format(subreddit)"
    headers = {"User-Agent": "0x16-api_advanced: project: \

    }
    params = {
         "limit": 10

    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
