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

    user_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{userId}")

    if user_response.status_code != 200:
        print(f"Error: User with ID {userId} not found.")
        sys.exit(1)

    user_name = user_response.json().get('name')

    todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={userId}")

    filename = f"{userId}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME",
                            "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_response.json():
            csv_writer.writerow(
                    [userId, user_name,
                     task.get('completed'), task.get('title')])

    print(f"Data has been exported to {filename} in CSV format.")
