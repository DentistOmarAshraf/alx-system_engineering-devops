#!/usr/bin/python3
"""
gather info from api using requests module
"""

import csv
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

    user_name = res_user.json()[0]["username"]
    user_all_task = res_todo.json()

    arr = []
    for x in user_all_task:
        new_arr = []
        new_arr.append(x["userId"])
        new_arr.append(user_name)
        new_arr.append(str(x["completed"]))
        new_arr.append(x["title"])
        arr.append(new_arr)

    with open(f"{user_all_task[0]['userId']}.csv", "w+") as f:
        writer = csv.writer(f, delimiter=",",
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for x in arr:
            writer.writerow(x)
