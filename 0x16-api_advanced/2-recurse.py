#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit: Name of the subreddit to fetch the hot posts for.
        hot_list: A list of the hot posts titles. Default is empty list.
        after: A token to specify which
        page of the results to fetch. Default is None.

    Returns:
        A list of hot posts titles or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    if after:
        url += f"&after={after}"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()["data"]
    posts = data["children"]
    after = data["after"]
    for post in posts:
        hot_list.append(post["data"]["title"])

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after=after)


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    hot_list = recurse(subreddit)
    if hot_list is None:
        print(f"Subreddit '{subreddit}' not found!")
    else:
        print(f"Number of hot posts: {len(hot_list)}")
        for i, title in enumerate(hot_list):
            print(f"{i + 1}. {title}")
