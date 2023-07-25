#!/usr/bin/python3
""" A module for fetching data using RESTFUL API"""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(sys.argv[1])).json()
    username = user_data.get("username")
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id, username, task.get("completed"), task.get("title")]
         ) for task in tasks]
