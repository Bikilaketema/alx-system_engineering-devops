#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: Name of the subreddit to fetch the top 10 hot posts for.

    Returns:
        None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Bikila/5.0 (Bicky; Biko; ket)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 400:
        print("None")
        return

    for post in response.json()["data"]["children"]:
        print(post["data"]["title"])


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)
