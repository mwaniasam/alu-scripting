#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        None: If the subreddit is invalid or there are no hot posts, None is printed.
    """
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            print(None)
            return

        for post in children:
            print(post.get("data", {}).get("title", None))

    except Exception:
        print(None)
