#!/usr/bin/python3
"""function to fetch Reddit API subscribers"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Funciton to fetch reddit API subscribers"""

    res = requests.get("https://www.reddit.com/r/{}/about/.json"
                       .format(subreddit),
                       allow_redirects=False)

    if res.status_code == 200:
        return int(res.json()["data"]["subscribers"])

    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
