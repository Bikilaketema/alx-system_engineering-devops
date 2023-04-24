#!/usr/bin/python3
"""
This module contains a script that generates a JSON file
containing a list of dictionaries of tasks for all employees.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_dict = {}
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = json.loads(response.text)

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_dict[user_id] = []

        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(url)
        tasks = json.loads(response.text)

        for task in tasks:
            task_dict = {"username": username,
                         "task": task.get("title"),
                         "completed": task.get("completed")}
            user_dict[user_id].append(task_dict)

    with open("todo_all_employees.json", mode="w") as f:
        json.dump(user_dict, f)
    print("All users found: OK")
