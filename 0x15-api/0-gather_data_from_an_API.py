#!/usr/bin/python3
"""
Retrive data form API
"""


import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users"
    user_data = url_user + "/" + user_id

    response = requests.get(user_data)
    todolist = requests.get(user_data + "/todos")

    emp_name = response.json().get("name")
    all_tasks = todolist.json()

    completed = 0
    done_tasks = []
    for task in all_tasks:
        if task.get('completed'):
            done_tasks.append(task)
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(done_tasks), len(all_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
