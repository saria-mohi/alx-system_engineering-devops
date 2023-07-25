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
    url_usr_data = "https://jsonplaceholder.typicode.com/users"
    user_data = url_usr_data + "/" + employee_id

    response = requests.get(user_data)
    todo_data = requests.get(user_data + "/todos")

    emp_name = response.json().get("name")
    total_task = todo_data.json()

    completed = 0
    task_list = []
    for task in total_task:
        if task.get('completed'):
            task_list.append(task)
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(task_list), len(total_task)))

    for task in task_list:
        print("\t {}".format(task.get('title')))