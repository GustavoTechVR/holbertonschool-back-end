#!/usr/bin/python3
""" API """
import requests
import sys


def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetching user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Fetching user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    return user_data, todo_data


def display_todo_progress(employee_id):
    user_data, todo_data = get_employee_data(employee_id)

    # Extracting relevant information
    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get("completed")]

    # Displaying the information
    print(f"Employee {employee_name} is done with
           tasks({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)
