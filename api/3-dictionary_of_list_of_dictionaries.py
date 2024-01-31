#!/usr/bin/python3
"""
Script to export data in JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    # Get user details
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    # Get user's tasks
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Create dictionary to store tasks
    tasks_dict = {user_id: []}

    for task in tasks_data:
        task_dict = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
        }
        tasks_dict[user_id].append(task_dict)

    # Export data to JSON file
    json_filename = '{}.json'.format(user_id)
    with open(json_filename, 'w') as json_file:
        json.dump(tasks_dict, json_file)
