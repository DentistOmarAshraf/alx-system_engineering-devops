#!/usr/bin/python3
"""
gather info from api using requests module
"""

import requests
import sys


if __name__ == "__main__":

    """
    gathering info from resful API
    """
    user_id = sys.argv[1]

    res_todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(user_id))
    res_user = requests.get(
            "https://jsonplaceholder.typicode.com/users?id={}"
            .format(user_id))

    user_name = res_user.json()[0]["name"]
    user_all_task = res_todo.json()

    completed = []
    for x in user_all_task:
        if x["completed"]:
            completed.append(x["title"])

    print("Employee {} is done with tasks ({}/{})"
          .format(user_name, len(completed), len(user_all_task)))

    for x in completed:
        print(" {}".format(x))
