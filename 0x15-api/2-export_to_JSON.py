#!/usr/bin/python3
""" Python script to export data in CSV format """


import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users"
    user_data = url_user + "/" + user_id

    response = requests.get(user_data)
    username = response.json().get('username')

    todos_path = user_data + "/todos"
    response = requests.get(todos_path)
    tasks = response.json()

    dic = {user_id: []}
    for task in tasks:
        dic[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username})

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(dic, json_file)
