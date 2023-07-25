#!/usr/bin/python3
"""
Model for fetch data from RESTFUL API
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

    e_name = response.json().get("name")
    all_tasks = todolist_data.json()

    done = 0
    done_tasks = []
    for task in all_tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1
    print("Employee {} is done with tasks({}/{}):".format(
        e_name, len(done_tasks), len(all_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
