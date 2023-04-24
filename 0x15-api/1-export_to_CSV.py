#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress and export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(url)
    user_response = requests.get(user_url)
    todos = response.json()
    user = user_response.json()

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user['id'], user['username'], todo['completed'], todo['title']])

    task_total = len(todos)
    completed_task = sum(task['completed'] for task in todos)

    print("Employee {} is done with tasks({}/{}):".format(user['name'], completed_task, task_total))
    for task in todos:
        if task['completed'] is True:
            print("\t {}".format(task['title']))

    print("Number of tasks in CSV: OK")

