#!/usr/bin/python3
"""Retrieve TODO list progress of a given employee ID from a REST API."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        api_url = "https://jsonplaceholder.typicode.com"
        employee = requests.get(api_url + "/users/{}".format(user_id)).json()
        todo_list =
        requests.get(api_url + "/todos", params={"userId": user_id}).json()

        completed_tasks = [task for task in todo_list if task["completed"]]
        progress = "{}/{}".format(len(completed_tasks), len(todo_list))

        print("Employee {} is done with tasks({}):"
                .format(employee["name"], progress))
        for task in completed_tasks:
            print("\t {}".format(task["title"]))
    else:
        print("Usage: ./0-gather_data_from_an_API.py USER_ID")
