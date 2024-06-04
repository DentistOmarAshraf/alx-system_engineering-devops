#!/usr/bin/python3
"""
Fetch ReditAPI
"""
import requests


def number_of_subscribers(subreddit):
    """Funciton to fetch reddit API subscribers"""
    res = requests.get("https://www.reddit.com/r/{}/about/.json"
                       .format(subreddit),
                       allow_redirects=False,
                       headers={"User-Agent": "My-Agent"})
    if res.status_code == 200:
        return int(res.json()["data"]["subscribers"])
    else:
        return 0
