#!/usr/bin/python3
"""returns information about TODO list progress in CSV format"""

import requests
import sys
import csv

if __name__ == "__main":
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

    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={userId}")
    todo_data = todos_response.json()

    totalTasks = len(todo_data)
    completed = sum(1 for task in todo_data if task.get('completed'))

    print('Employee {} is done with tasks({}/{}):'.format(user_name, completed, totalTasks))

    for task in todo_data:
        if task.get('completed'):
            print('\t' + task.get('title'))

    filename = f"{userId}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            csv_writer.writerow([userId, user_name, task.get('completed'), task.get('title')])

    print(f"Data has been exported to {filename} in CSV format.")
