#!/usr/bin/python3
"""
Python script that returns information
about employee todo list progress
"""


import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users"
    user_data = url_user + "/" + emp_id

    response = requests.get(user_data)
    todo_data = requests.get("https://jsonplaceholder.typicode.com/todos")

    emp_name = response.json().get("name")
    total_tasks = todo_data.json()

    completed = 0
    list_tasks = []
    for task in total_tasks:
        if task.get('completed'):
            list_tasks.append(task)
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(list_tasks), len(total_tasks)))

    for task in list_tasks:
        print("\t {}".format(task.get('title')))
