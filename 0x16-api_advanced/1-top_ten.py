#!/usr/bin/python3
"""
fetch API
"""
import requests


def top_ten(subreddit):
    res = requests.get("https://www.reddit.com/r/{}/hot/.json"
                       .format(subreddit),
                       headers={"User-agent": "My-Agent"},
                       allow_redirects=False)
    if res.status_code == 200:
        x = 0
        for title in res.json()["data"]["children"]:
            x = x + 1
            print(title["data"]["title"])
            if x == 9:
                break


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
