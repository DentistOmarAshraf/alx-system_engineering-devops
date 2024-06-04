#!/usr/bin/python3
"""function to fetch Reddit API subscribers"""

import requests
import sys


def number_of_subscribers(subreddit):
    res = requests.get(f"https://www.reddit.com/r/{subreddit}/about/.json",
                       headers={"User-agent": "My-Agent"},
                       allow_redirects=False)
    if res.status_code == 200:
        return int(res.json()["data"]["subscribers"])
    return 0
