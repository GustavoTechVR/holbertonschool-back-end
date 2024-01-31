#!/usr/bin/python3
""" API """
import requests
import csv
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

def export_to_csv(employee_id, user_data, todo_data):
    employee_name = user_data.get("username")

    # Creating CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Writing header
        writer.writeheader()

        # Writing tasks data
        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
            })

    print(f"Data exported to {filename}")

def display_todo_progress(employee_id):
    user_data, todo_data = get_employee_data(employee_id)

    # Extracting relevant information
    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get("completed")]

    # Displaying the information
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task.get('title')}")

    # Exporting to CSV
    export_to_csv(employee_id, user_data, todo_data)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)
