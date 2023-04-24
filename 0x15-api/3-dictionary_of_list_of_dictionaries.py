#!/usr/bin/python3
"""
This module defines a function that retrieves all tasks from the given
REST API endpoint and exports them to a JSON file.
"""

import json
import requests
from sys import argv


def export_all_to_json():
    """Exports all tasks from the given REST API endpoint to a JSON file."""
    url = 'https://jsonplaceholder.typicode.com/todos/'
    users_url = 'https://jsonplaceholder.typicode.com/users/'

    tasks = requests.get(url).json()
    users = requests.get(users_url).json()

    if not tasks:
        print("No tasks found")
        return

    # create a dictionary to hold tasks for all users
    tasks_by_user = {}

    for user in users:
        user_id = user['id']
        user_name = user['username']
        tasks_by_user[user_id] = []

    # populate the dictionary with tasks for all users
    for task in tasks:
        user_id = task['userId']
        task_dict = {}
        task_dict['username'] = [user['username'] for user in users if user['id'] == user_id][0]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        tasks_by_user[user_id].append(task_dict)

    # write the dictionary to a JSON file
    with open("todo_all_employees.json", 'w') as file:
        json.dump(tasks_by_user, file)


if __name__ == '__main__':
    export_all_to_json()
