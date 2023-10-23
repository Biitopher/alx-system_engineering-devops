#!/usr/bin/python3
"""Python script using REST API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    userId = sys.argv[1]

    user_response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(userId))

    if user_response.status_code != 200:
        print(f"Error: User with ID {userId} not found.")
        sys.exit(1)

    user_data = user_response.json()
    user_name = user_data.get('name')

    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = todos_response.json()

    totalTasks = 0
    completed = 0

    for task in todo_data:
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todo_data
          if task.get('userId') == int(userId) and task.get('completed')]))
