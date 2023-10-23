#!/usr/bin/python3
"""Python script using REST API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    userId = sys.argv[1]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")

    if user_response.status_code != 200:
        print(f"Error: User with ID {userId} not found.")
        sys.exit(1)

    user_data = user_response.json()
    user_name = user_data.get('name')

    # Fetch the user's TODO list
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={userId}")
    todo_data = todos_response.json()

    totalTasks = len(todo_data)
    completed = sum(1 for task in todo_data if task.get('completed'))

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, completed, totalTasks))

    for task in todo_data:
        if task.get('completed'):
            print('\t' + task.get('title'))
