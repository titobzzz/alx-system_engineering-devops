#!/usr/bin/python3
"""Function to query for  subscribers on aReddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returne totalnumber of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    if  response.status_code == 200:
         results = response.json().get("data")
         return results.get("subscribers")
