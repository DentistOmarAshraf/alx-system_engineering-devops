#!/usr/bin/python3
"""
gather info from api using requests module
"""

import json
import requests


if __name__ == "__main__":

    """
    gathering info from resful API
    """

    res_user = requests.get(
            "https://jsonplaceholder.typicode.com/users")

    user_all = res_user.json()

    all_tog = {}
    for x in user_all:
        res_todo = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(x["id"]))
        user_todo = res_todo.json()

        arr = []
        user_name = x["username"]
        for y in user_todo:
            dic = {}
            dic["username"] = user_name
            dic["task"] = y["title"]
            dic["completed"] = y["completed"]
            arr.append(dic)

        all_tog[x["id"]] = arr

    with open("todo_all_employees.json", "w+") as f:
        json.dump(all_tog, f, indent=4)
