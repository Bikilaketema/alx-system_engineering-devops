#!/usr/bin/python3
"""Recursively queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """ Recursively queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit: Name of the subreddit to fetch the hot posts for.
        hot_list: A list of the hot posts titles. Default is empty list.
        after: A token to specify which page
        of the results to fetch. Default is None.

    Returns:
        A list of hot posts titles or None if the subreddit is invalid.
        """
    global after
    headers = {'User-Agent': 'BikcyKet'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, params=parameters, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
