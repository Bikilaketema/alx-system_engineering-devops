#!/usr/bin/python3
"""
This script exports data in the JSON format for a given employee ID.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    # Set up the API endpoints
    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = base_url + "users/{}"
    todos_url = base_url + "todos?userId={}"

    # Retrieve the user's name
    user_id = argv[1]
    user_response = requests.get(users_url.format(user_id))
    user = user_response.json()
    username = user.get("username")

    # Retrieve the user's tasks
    tasks_response = requests.get(todos_url.format(user_id))
    tasks = tasks_response.json()

    # Format the tasks as a dictionary with the user ID as the key
    tasks_dict = {user_id: []}
    for task in tasks:
        task_dict = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": username}
        tasks_dict[user_id].append(task_dict)

    # Write the tasks to a JSON file
    filename = "{}.json".format(user_id)
    with open(filename, mode="w") as f:
        json.dump(tasks_dict, f)
