#!/usr/bin/python3
"""
Fetch ReditAPI
"""
import requests


def number_of_subscribers(subreddit):
    """Funciton to fetch reddit API subscribers"""
    res = requests.get(f"https://www.reddit.com/r/{subreddit}/about/.json")
    if res.status_code == 200:
        return res.json()["data"]["subscribers"]
    return 0
