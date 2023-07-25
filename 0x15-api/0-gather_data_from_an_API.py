#!/usr/bin/python3
"""
Python script that returns information
about employee todo list progress
"""


import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url_user_data = "https://jsonplaceholder.typicode.com/users"
    user_data = url_user_data + "/" + employee_id

    response = requests.get(user_data)
    todo_data = requests.get(user_data + "/todos")

    emp_name = response.json().get("name")

    tasks = todo_data.json()

    total_task = 0
    list_tasks = []
    for task in tasks:
        if task.get('completed'):
            list_tasks.append(task)
            total_task += 1
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(list_tasks), len(tasks)))

    for task in list_tasks:
        print("\t {}".format(task.get('title')))
