#!/usr/bin/python3
"""
Queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "myBot/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    data = response.json()
    return data["data"]["subscribers"]
