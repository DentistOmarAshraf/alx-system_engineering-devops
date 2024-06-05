#!/usr/bin/python3
"""function to fetch Reddit API subscribers"""

import requests
import sys


def number_of_subscribers(subreddit):
    if subreddit is None or subreddit == "":
        return 0
    res = requests.get(f"https://www.reddit.com/r/{subreddit}/about/.json",
                       headers={"User-agent": "My-Agent"},
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get("data").get("subscribers")
        return int(data)
    return 0
