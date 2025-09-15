import argparse
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            # Ensure all tasks are dictionaries with expected keys
            for i, task in enumerate(tasks):
                if isinstance(task, str):
                    tasks[i] = {"task": task, "done": False}
                elif not isinstance(task, dict) or "task" not in task or "done" not in task:
                    # Handle malformed entries if necessary, here we'll just remove them
                    tasks.pop(i)
            return tasks
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def add_task(task_description):
    """Adds a new task to the list."""
    tasks = load_tasks()
    tasks.append({"task": task_description, "done": False})
    save_tasks(tasks)
    print(f"Added task: \"{task_description}\"")

def list_tasks():
    """Lists all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "X" if task["done"] else " "
        print(f"{i}. [{status}] {task['task']}")

def complete_task(task_number):
    """Marks a task as complete."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        if tasks[task_number - 1]["done"]:
            print(f"Task {task_number} is already marked as done.")
        else:
            tasks[task_number - 1]["done"] = True
            save_tasks(tasks)
            print(f"Marked task {task_number} as done.")
    else:
        print("Invalid task number.")

def main():
    """Main function to parse arguments and call appropriate functions."""
    # Set the working directory to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    parser = argparse.ArgumentParser(description="A simple command-line to-do list application.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The description of the task")

    # 'list' command
    subparsers.add_parser("list", help="List all tasks")

    # 'done' command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("task_number", type=int, help="The number of the task to mark as done")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.task_number)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
