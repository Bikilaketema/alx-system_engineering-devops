#!/usr/bin/python3
"""
Export data from the JSONPlaceholder API to JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(api_url + '/users').json()
    tasks = requests.get(api_url + '/todos').json()

    # Create dictionary to store tasks for each user
    user_tasks = {}
    for user in users:
        user_id = user['id']
        user_name = user['username']
        user_tasks[user_id] = []
        for task in tasks:
            if task['userId'] == user_id:
                task_dict = {
                    'username': user_name,
                    'task': task['title'],
                    'completed': task['completed']
                }
                user_tasks[user_id].append(task_dict)

    # Write data to file in JSON format
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(user_tasks, file)
