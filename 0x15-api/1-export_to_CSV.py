#!/usr/bin/python3
"""Python script using REST API and exporting data to CSV"""

import requests
import sys
import csv

if __name__ == "__main":
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
    user_id = user_data.get('id')
    user_name = user_data.get('name')

    todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos")
    todo_data = todos_response.json()

    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"])

        csv_writer.writerows(completedTasks)

    for task in todo_data:
        if task.get('userId') == int(userId):
            cvs_writer.writerow([userId, user_name, str(task.get('completed')),
                                 task.get('title')])
