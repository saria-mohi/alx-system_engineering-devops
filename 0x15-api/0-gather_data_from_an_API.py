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
    initial_url = "https://jsonplaceholder.typicode.com/users"
    url = initial_url + "/" + employee_id

    response = requests.get(url)
    todolist_data = requests.get(url + "/todos")
    """print(todolist_data.json())"""

    e_name = response.json().get("name")
    """print(e_name)"""
    all_tasks = todolist_data.json()
    """print(all_tasks)"""

    done = 0
    done_tasks = []
    for task in all_tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1
    """print(done_tasks)"""
    print("Employee {} is done with tasks({}/{}):".format(
        e_name, len(done_tasks), len(all_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
