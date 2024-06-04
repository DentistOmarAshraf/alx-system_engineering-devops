#!/usr/bin/python3
"""
Fetch ReditAPI
"""
import requests


def number_of_subscribers(subreddit):
    """Funciton to fetch reddit API subscribers"""
    head = {"User-agent": "Windows NT 10.0; Win64; x64"}
    res = requests.get(f"https://www.reddit.com/r/{subreddit}/about/.json",
                       allow_redirects=False, headers=head)
    if res.status_code == 200:
        return res.json()["data"]["subscribers"]
    return 0
