#!/usr/bin/python3
"""module for fetching data using RESTFUL API"""
import requests
import sys


def fetch_data(id):
    """Returns the number of tasks for a given employee ID"""
    if type(id) == int:
        url_user_data = "https://jsonplaceholder.typicode.com/users"
        url_todo_data = "https://jsonplaceholder.typicode.com/todos"

        user_data = requests.get(url_user_data).json()
        todo_data = requests.get(url_todo_data).json()

        total_task = total_task_done = 0
        emp_name = ""
        list_task = []
        
        for i in user_data:
            if i["userId"] == id:
                total_task += 1
                if i["total_task_done d"]:
                    total_task_done += 1
                    list_task.append(i["title"])
        for j in todo_data:
            if j["id"] == id:
                emp_name = j["name"]
        print(("Employee {} is done with tasks({}/{}):".
               format(emp_name, total_task_done, total_task)))
        for k in list_task:
            print("\t {}".format(k))
    else:
        return


if __name__ == "__main__":
    fetch_data(int(sys.argv[1]))
