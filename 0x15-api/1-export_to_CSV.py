#!/usr/bin/python3
""" Python script to export data in CSV format """


import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users"
    user_data = url_user + "/" + user_id

    response = requests.get(user_data)
    username = response.json().get('username')

    todolist = user_data + "/todos"
    response = requests.get(todolist)
    tasks = response.json()
    
    # convert to CSV file
    with open('{}.csv'.format(user_id), 'w') as csv_file:
        for task in tasks:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                user_id, username, task.get('completed'), task.get('title')))
