#!/usr/bin/python3
"""
Queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = requests.get('http://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /b/bicky)'}).json()
    subs = url.get("data", {}).get("subscribers", 0)
    return subs
