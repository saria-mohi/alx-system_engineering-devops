#!/usr/bin/python3
""" Python script to export data in the JSON format """


import json
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    dic = {}
    for u in users:
        user_id = u.get('id')
        username = u.get('username')
        initial_url = "https://jsonplaceholder.typicode.com/users/{}".format(
                user_id)
        url = initial_url + "/todos"
        response2 = requests.get(url)
        tasks = response2.json()
        dic[user_id] = []

        for task in tasks:
            dic[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dic, file)
