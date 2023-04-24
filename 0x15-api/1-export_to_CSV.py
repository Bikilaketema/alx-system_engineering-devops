#!/usr/bin/python3
"""Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress, and exports it to CSV."""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    # Get user id from command line arguments
    user_id = argv[1]
    # Get user info
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    # Get user's todo list
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    .format(user_id)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    # Export data to CSV file
    file_name = "{}.csv".format(user_id)
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            task_completed_status = str(todo['completed'])
            task_title = todo['title']
            writer.writerow([user_id, user_data['username'],
                            task_completed_status, task_title])
    # Print feedback message
    print("Number of tasks in CSV: OK")
