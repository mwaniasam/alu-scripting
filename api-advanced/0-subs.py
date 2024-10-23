#!/usr/bin/python3
""""A  function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """"Doc"""
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        return 0
    else:
        json_response = res.json()
        return json_response.get('data').get('subscribers')
