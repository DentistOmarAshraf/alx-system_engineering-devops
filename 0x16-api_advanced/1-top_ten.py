#!/usr/bin/python3
"""
fetch API
"""
import requests


def top_ten(subreddit):
    res = requests.get("https://www.reddit.com/r/{}/hot/.json?limit=10"
                       .format(subreddit),
                       headers={"User-agent": "My-Agent"},
                       allow_redirects=False)
    if res.status_code == 200:
        for title in res.json()["data"]["children"]:
            print((title["data"]["title"]))
    else:
        print(None)
