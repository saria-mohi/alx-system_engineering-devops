#!/usr/bin/python3
"""module for fetching data using RESTFUL API"""

import json
import requests
import sys


def fetch_data(id):
    """fetch data base on the id and process data"""
    user_id = sys.argv[1]
    url_user_data = "https://jsonplaceholder.typicode.com/users"
    url_todo_data = "https://jsonplaceholder.typicode.com/todos"

    user_data = requests.get(url_user_data).json()
    todo_data = requests.get(url_todo_data).json()
    username = user_data.get("username")
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo_data]}, jsonfile)



if __name__ == "__main__":
    fetch_data(int(sys.argv[1]))
