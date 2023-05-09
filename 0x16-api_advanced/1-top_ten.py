#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""


import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: Name of the subreddit to fetch the top 10 hot posts for.

    Returns:
        None.
    """
    url = f"https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Bikila/5.0 (Bicky; Biko; ket)"}
    response = requests.get(url, headers=headers, allow_redirects=False,params=parameters)
    parameters = {'limit': 10}

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
