#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the top ten hot posts for a given subreddit.
    Print None if an invalid subreddit is given.
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Check response status before calling .json()
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    if not data:
        print(None)
        return

    for post in data:
        print(post.get('data', {}).get('title'))

