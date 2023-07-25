#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_data = requests.get("https://jsonplaceholder.typicode.com/users".format(user_id)).json()
    username = user_data.get("username")
    todo_data = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo_data]}, jsonfile)
