#!/usr/bin/python3
"""Module 0-gather_data_from_an_API.py"""
import csv
import requests
import sys


def to_do(num):
    """Returns the number of tasks for a given employee ID"""
    if type(num) == int:
        url_todo = "https://jsonplaceholder.typicode.com/todos"
        url_user = "https://jsonplaceholder.typicode.com/users"

        raw_todo = requests.get(url_todo).json()
        raw_user = requests.get(url_user).json()

        emp_name = ""
        emp_id = 0
        py_form = []
        for j in raw_user:
            if j["id"] == num:
                emp_name = j["username"]
        for i in raw_todo:
            if i["userId"] == num:
                emp_id = i["userId"]
                py_form.append("{}, {}, {}, {}".
                               format(i["userId"],
                                      emp_name,
                                      i["completed"],
                                      i["title"]))
        file = "{}.csv".format(emp_id)
        with open(file, mode="w", newline="") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            for k in py_form:
                csv_form = [val.strip() for val in k.split(", ")]
                wr.writerow(csv_form)

    else:
        return


if __name__ == "__main__":
    to_do(int(sys.argv[1]))