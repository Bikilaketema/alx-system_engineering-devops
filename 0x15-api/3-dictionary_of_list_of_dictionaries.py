#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    users_req = requests.get(api_url + "users")
    todos_req = requests.get(api_url + "todos")

    users_data = users_req.json()
    todos_data = todos_req.json()

    todo_all_employees = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        tasks = []
        for todo in todos_data:
            if todo.get("userId") == user_id:
                task = {"username": username,
                        "task": todo.get("title"),
                        "completed": todo.get("completed")}
                tasks.append(task)

        todo_all_employees[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_all_employees, json_file)
