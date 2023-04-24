#!/usr/bin/python3
"""
Exports tasks owned by an employee to a CSV file
"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    try:
        employee_id = int(sys.argv[1])
    except (IndexError, ValueError):
        sys.stderr.write("Usage: ./1-export_to_CSV.py employee_id\n")
        sys.exit(1)

    employee_req = requests.get(url + "users/{}".format(employee_id))
    employee = employee_req.json()
    employee_name = employee.get("username")

    tasks_req = requests.get(url + "todos", params={"userId": employee_id})
    tasks = tasks_req.json()

    with open('{}.csv'.format(employee_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])

