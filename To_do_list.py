import os
import json
from datetime import datetime

# File path to store the to-do list data
TODO_FILE = "todo_list.json"

def load_todo_list():
    """Load the to-do list data from a file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            try:
                todo_list = json.load(file)
            except json.JSONDecodeError:
                todo_list = []
    else:
        todo_list = []
    return todo_list

def save_todo_list(todo_list):
    """Save the to-do list data to a file."""
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=2)

def display_todo_list(todo_list):
    """Display the current to-do list."""
    print("\n--- To-Do List ---")
    if not todo_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['task']} - {task['created_at']}")

def add_task(todo_list):
    """Add a task to the to-do list."""
    task_description = input("Enter the task: ")
    new_task = {"task": task_description, "created_at": str(datetime.now())}
    todo_list.append(new_task)
    save_todo_list(todo_list)
    print(f"Task '{task_description}' added successfully.")

def mark_task_completed(todo_list):
    """Mark a task as completed."""
    display_todo_list(todo_list)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        todo_list[task_index]["completed_at"] = str(datetime.now())
        save_todo_list(todo_list)
        print("Task marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    """Main function to manage the To-Do List."""
    todo_list = load_todo_list()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_task_completed(todo_list)
        elif choice == "4":
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
