#!/usr/bin/python3
""" Python script to export data in CSV format """


import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    initial_url = "https://jsonplaceholder.typicode.com/users"
    url = initial_url + "/" + user_id

    response = requests.get(url)
    username = response.json().get('username')

    todos_path = url + "/todos"
    response = requests.get(todos_path)
    tasks = response.json()

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        for task in tasks:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                user_id, username, task.get('completed'), task.get('title')))
