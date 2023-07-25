#!/usr/bin/python3
""" A module for fetching data using RESTFUL API"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(sys.argv[1])).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos", 
                         params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for task in tasks if task.
                 get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]
