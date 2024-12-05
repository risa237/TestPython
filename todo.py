import os

TODO_FILE = 'todo_list.txt'

class Task:
    def __init__(self, description, priority=3, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] (Priority: {self.priority}) {self.description}"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        tasks = []
        for line in file:
            description, priority, completed = line.strip().split('|')
            tasks.append(Task(description, int(priority), completed == 'True'))
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task.description}|{task.priority}|{task.completed}\n")

def add_task(description, priority):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(Task(description, priority))
    save_tasks(tasks)
    print(f'Task "{description}" added with priority {priority}.')

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(task_number):
    """Delete a task by its number."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task.description}" deleted.')
    else:
        print("Invalid task number.")

def mark_task_completed(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1].completed = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_number - 1].description}" marked as completed.')
    else:
        print("Invalid task number.")

def edit_task(task_number, new_description, new_priority):
    """Edit a task's description and priority."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1].description = new_description
        tasks[task_number - 1].priority = new_priority
        save_tasks(tasks)
        print(f'Task {task_number} updated.')
    else:
        print("Invalid task number.")

def search_tasks(keyword):
    """Search for tasks containing a keyword."""
    tasks = load_tasks()
    found_tasks = [task for task in tasks if keyword.lower() in task.description.lower()]
    if not found_tasks:
        print(f"No tasks found containing '{keyword}'.")
    else:
        print(f"Tasks containing '{keyword}':")
        for idx, task in enumerate(found_tasks, start=1):
            print(f"{idx}. {task}")

def sort_tasks(by='priority'):
    """Sort tasks by priority or completion status."""
    tasks = load_tasks()
    if by == 'priority':
        tasks.sort(key=lambda x: x.priority)
    elif by == 'completed':
        tasks.sort(key=lambda x: x.completed)
    save_tasks(tasks)
    print(f"Tasks sorted by {by}.")

def main():
    """Main function to run the to-do list application."""
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Edit task")
        print("6. Search tasks")
        print("7. Sort tasks by priority")
        print("8. Sort tasks by completion status")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            description = input("Enter the task description: ")
            try:
                priority = int(input("Enter the task priority (1-5): "))
                if priority < 1 or priority > 5:
                    raise ValueError
                add_task(description, priority)
            except ValueError:
                print("Please enter a valid priority (1-5).")
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to edit: "))
                new_description = input("Enter the new task description: ")
                new_priority = int(input("Enter the new task priority (1-5): "))
                edit_task(task_number, new_description, new_priority)
            except ValueError:
                print("Please enter valid inputs.")
        elif choice == '6':
            keyword = input("Enter the keyword to search for: ")
            search_tasks(keyword)
        elif choice == '7':
            sort_tasks(by='priority')
        elif choice == '8':
            sort_tasks(by='completed')
        elif choice == '9':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
