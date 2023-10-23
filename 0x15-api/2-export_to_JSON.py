#!/usr/bin/python3
"""Python script using REST API and exporting data to JSON"""

if __name__ == "__main__":

    import csv
    import requests
    import sys
    import json

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_response = todos_response.json()

    todoUser = {}
    taskList = []

    for task in todos_response:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as csv_file:
        json.dump(todoUser, csv_file)
