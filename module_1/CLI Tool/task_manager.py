import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file"""
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
        return True
    except IOError:
        print("Error: Could not save tasks to file")
        return False

def generate_task_id(tasks):
    """Generate a unique ID for a new task"""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task():
    if len(sys.argv) < 3:
        print("Error: Please provide a task description")
        print("Usage: python3 task_manager.py add <task>")
        return
    
    # Join all arguments after 'add' to form the task description
    task_description = ' '.join(sys.argv[2:])
    
    tasks = load_tasks()
    new_task = {
        'id': generate_task_id(tasks),
        'description': task_description,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    
    if save_tasks(tasks):
        print(f"✓ Added task: '{task_description}' (ID: {new_task['id']})")
    else:
        print("✗ Failed to add task")

def list_tasks():
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found. Add some tasks with 'add <task>'")
        return
    
    print(f"\n{'ID':<4} {'Status':<10} {'Task'}")
    print("-" * 50)
    
    for task in tasks:
        status = "✓ Done" if task['completed'] else "○ Pending"
        print(f"{task['id']:<4} {status:<10} {task['description']}")
    
    completed_count = sum(1 for task in tasks if task['completed'])
    total_count = len(tasks)
    print(f"\nTotal: {total_count} tasks ({completed_count} completed)")

def complete_task():
    if len(sys.argv) < 3:
        print("Error: Please provide a task ID")
        print("Usage: python3 task_manager.py complete <id>")
        return
    
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print("Error: Task ID must be a number")
        return
    
    tasks = load_tasks()
    task_found = False
    
    for task in tasks:
        if task['id'] == task_id:
            if task['completed']:
                print(f"Task {task_id} is already completed!")
            else:
                task['completed'] = True
                if save_tasks(tasks):
                    print(f"✓ Completed task: '{task['description']}'")
                else:
                    print("✗ Failed to update task")
            task_found = True
            break
    
    if not task_found:
        print(f"Error: Task with ID {task_id} not found")

def delete_task():
    if len(sys.argv) < 3:
        print("Error: Please provide a task ID")
        print("Usage: python3 task_manager.py delete <id>")
        return
    
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print("Error: Task ID must be a number")
        return
    
    tasks = load_tasks()
    original_length = len(tasks)
    
    # Filter out the task with the given ID
    tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(tasks) == original_length:
        print(f"Error: Task with ID {task_id} not found")
        return
    
    if save_tasks(tasks):
        print(f"✓ Deleted task with ID {task_id}")
    else:
        print("✗ Failed to delete task")

def show_help():
    print("Task Manager - Manage your tasks from the command line")
    print("\nUsage:")
    print("  python3 task_manager.py <command> [arguments]")
    print("\nCommands:")
    print("  add <task>     - Add a new task")
    print("  list          - List all tasks")
    print("  complete <id> - Mark task as complete")
    print("  delete <id>   - Delete a task")
    print("  help          - Show this help")

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "help":
        show_help()
    elif command == "add":
        add_task()
    elif command == "list":
        list_tasks()
    elif command == "complete":
        complete_task()
    elif command == "delete":
        delete_task()
    else:
        print(f"Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main()