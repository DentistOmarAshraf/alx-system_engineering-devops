#!/usr/bin/python3
"""
gather info from api using requests module
"""

import os
import json
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
        new_dic = {}
        new_dic["username"] = user_name
        new_dic["task"] = x["title"]
        new_dic["completed"] = x["completed"]
        arr.append(new_dic)

    if not os.path.exists("todo_all_employees.json"):
        with open("todo_all_employees.json", "w") as f:
            json.dump({}, f)

    with open("todo_all_employees.json", "r") as f:
        all_tog = json.load(f)

    all_tog[f"{user_all_task[0]['userId']}"] = arr

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tog, f, indent=4)
