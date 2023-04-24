#!/usr/bin/python3
"""
Python script that, using the provided REST API,
for a given employee ID, returns information about
their todo list progress and exports it to a CSV file
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    # API endpoint URLs
    api_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(api_url)
    todos_url = "{}/todos".format(api_url)

    # Check command line arguments
    if len(argv) != 2:
        print("Usage: {} USER_ID".format(argv[0]))
        exit(1)

    # Get the user by ID
    user_id = argv[1]
    user = requests.get("{}/{}?id={}".format(users_url, user_id, user_id)).json()

    if not user:
        print("User with ID {} doesn't exist".format(user_id))
        exit(1)

    # Get the user's todo list by ID
    todo_list = requests.get("{}?userId={}".format(todos_url, user_id)).json()

    # Create the CSV file
    filename = "{}.csv".format(user_id)

    with open(filename, mode="w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write the header row
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write the todo list rows
        for task in todo_list:
            writer.writerow([
                user_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])

    print("Todo list exported to {}".format(filename))

