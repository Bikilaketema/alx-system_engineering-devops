import json
import requests
from sys import argv


def export_all_to_json():
    # Endpoint URLs for tasks and users
    url = 'https://jsonplaceholder.typicode.com/todos/'
    users_url = 'https://jsonplaceholder.typicode.com/users/'

    # Retrieve tasks and users from the API
    tasks = requests.get(url).json()
    users = requests.get(users_url).json()

    # Check if tasks are empty
    if not tasks:
        print("No tasks found")
        return

    # Create a dictionary to hold tasks for all users
    tasks_by_user = {}

    # Populate the dictionary with empty lists for each user
    for user in users:
        user_id = user['id']
        tasks_by_user[user_id] = []

    # Populate the dictionary with tasks for all users
    for task in tasks:
        user_id = task['userId']
        task_dict = {}

        # Add task details to a dictionary
        task_dict['username'] = [user['username'] for user in users if user['id'] == user_id][0]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']

        # Append the task dictionary to the list of tasks for the user
        tasks_by_user[user_id].append(task_dict)

    # Write the dictionary to a JSON file
    with open("todo_all_employees.json", 'w') as file:
        json.dump(tasks_by_user, file)


if __name__ == '__main__':
    export_all_to_json()
