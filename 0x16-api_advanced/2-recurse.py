#!/usr/bin/python3
"""
Recursive Fetch from api
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Function to Fetch all hot titles"""
    if after is None or after == "":
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}"

    head = {"User-agent": "My-agent"}
    res = requests.get(url, allow_redirects=False, headers=head)
    if res.status_code != 200:
        return None

    next_page = res.json().get("data").get("after")
    topic_info = res.json().get("data").get("children")
    for topic in topic_info:
        hot_list.append(topic.get("data").get("title"))

    if next_page is None:
        return hot_list

    return recurse(subreddit, hot_list, next_page)
