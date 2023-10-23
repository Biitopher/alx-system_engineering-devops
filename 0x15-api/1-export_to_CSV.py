#!/usr/bin/python3
"""Python script using REST API and exporting data to CSV"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    user_name = user.json().get('username')
    todos_response = requests.get(
            'https://jsonplaceholder.typicode.com/todos')

    filename = userId + '.csv'
    with open(filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos_response.json():
            if task.get('userId') == int(userId):
                csv_writer.writerow([userId, user_name, str(task.get(
                    'completed')), task.get('title')])
