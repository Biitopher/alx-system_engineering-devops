#!/usr/bin/python3
"""Python script using REST API and exporting data to JSON"""

if __name__ == "__main__":

    import sys
    import requests
    import csv
    import json

    user_response = requests.get("https://jsonplaceholder.typicode.com/users")

    user_data = user_response.json()
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_data = todos_response.json()
    todo_All = {}

    for user in user_data:
        taskList = []
        for task in todo_data:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todo_All[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as csv_file:
        json.dump(todo_All, csv_file)
