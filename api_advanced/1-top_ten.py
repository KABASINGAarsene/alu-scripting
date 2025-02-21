#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the
top ten hot posts of a given subreddit. Prints None if the subreddit is invalid.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the top ten hot posts for a given subreddit.
    Print None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'
    }

    # Make the request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get('data', {}).get('title'))
