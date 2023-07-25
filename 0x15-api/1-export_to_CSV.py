#!/usr/bin/python3
"""Module 0-gather_data_from_an_API.py"""
import csv
import requests
import sys


def fetch_data(id):
    """Returns the number of tasks for a given employee ID"""
    if type(id) == int:
        url_user_data = "https://jsonplaceholder.typicode.com/users"
        url_todo_data = "https://jsonplaceholder.typicode.com/todos"

        user_data = requests.get(url_user_data).json()
        todo_data = requests.get(url_todo_data).json()

        emp_name = ""
        emp_id = 0
        emp_list = []
        for j in user_data:
            if j["id"] == id:
                emp_name = j["username"]
        for i in todo_data:
            if i["userId"] == id:
                emp_id = i["userId"]
                emp_list.append("{}, {}, {}, {}".
                                format(i["userId"],
                                       emp_name,
                                       i["completed"],
                                       i["title"]))
        file = "{}.csv".format(emp_id)
        with open(file, mode="w", newline="") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            for k in emp_list:
                csv_form = [val.strip() for val in k.split(", ")]
                wr.writerow(csv_form)

    else:
        return


if __name__ == "__main__":
    fetch_data(int(sys.argv[1]))