#!/usr/bin/python3
"""
Recursive Fetch from api
"""

import requests


def recurse(subreddit, hot_list=[]):

    if len(hot_list) > 0 and hot_list[-1]["after"] is None:
        to_ret = []
        for item in hot_list:
            to_ret = to_ret + item["children"]
        return to_ret

    if len(hot_list) > 0:
        url = "https://www.reddit.com/r/{}/hot/.json?limit=10&after={}"
        res = requests.get(url.format(subreddit, hot_list[-1]["after"]),
                           allow_redirects=False)

    else:
        res = requests.get("https://www.reddit.com/r/{}/hot/.json?limit=10"
                           .format(subreddit),
                           allow_redirects=False)
    dt = {}
    if res.status_code == 200:
        dt["after"] = res.json()["data"]["after"]
        dt["children"] = []
        for title in res.json()["data"]["children"]:
            dt["children"].append(title["data"]["title"])
        hot_list.append(dt)

    return recurse(subreddit, hot_list)
