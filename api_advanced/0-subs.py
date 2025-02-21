#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return number of subscribers for a given subreddit.
    Return 0 if an invalid subreddit is given.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set custom User-Agent to avoid rate limiting
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Prevent following redirects and handle status codes properly
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if request is successful
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
