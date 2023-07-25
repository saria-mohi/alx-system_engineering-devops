#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(sys.argv[1])).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": sys.argv[1]}).json()
    username = user_data.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in tasks]
