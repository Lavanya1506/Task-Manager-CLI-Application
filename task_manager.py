# Dummy login credentials
DUMMY_EMAIL = "test@example.com"
DUMMY_PASSWORD = "password123"

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False
        
#  Call login outside the function and keep asking until successful
while not login():
    print("Please try logging in again.")
  


# Define a task Class

class Task:
    def __init__(self, task_id, title, due_date, completed=False):
        self.task_id = task_id
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def __repr__(self):
        return f"Task(id={self.task_id}, title='{self.title}', due_date='{self.due_date}', completed={self.completed})"




# Save tasks to a File
import json

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

# Load Task From A File
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [
                Task(
                    task_id=task.get('task_id', task.get('id')),  # Use 'id' if 'task_id' is missing
                    title=task['title'],
                    due_date=task.get('due_date', 'No Due Date'),  # Default to a message if 'due_date' is missing
                    completed=task.get('completed', False)
                )
                for task in tasks_data
            ]
    except FileNotFoundError:
        print("No tasks found. (if the file is empty or not available)")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the format of tasks.json.")
        return []



# 1.Add Task
def add_task(tasks, title, due_date):
    if tasks:
        highest_id = max(task.task_id for task in tasks)
        task_id = highest_id + 1
    else:
        task_id = 1
    
    new_task = Task(task_id, title, due_date)
    tasks.append(new_task)
    print(f"Task '{title}' added with ID {task_id} and Due Date {due_date}.")

# 2.View task
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            print(f"{task.task_id}. {status} {task.title} - Due: {task.due_date}")

# 3.Delete task
def delete_task(tasks, task_id):
    task_found = False
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted.")
            task_found = True
            break
    if not task_found:
        print(f"Task {task_id} not found.")

4.# Mark Task Complete:
def mark_task_complete(tasks, task_id):
    task_found = False
    for task in tasks:
        if task.task_id == task_id:
            task.completed = True
            print(f"Task {task_id} marked as complete!")
            task_found = True
            break
    if not task_found:
        print(f"Task {task_id} not found.")

# 5.Create a Command-Line Interface (CLI)

def main():
    tasks = load_tasks()

    print("Welcome to Task Manager CLI!")
    print("Loading tasks from tasks.json...")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Save and Exit")
        
        choice = input("Choose your choice: ")
        
        if choice == '1':
            title = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, due_date)
            print("Task added successfully!")
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            try:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(tasks, task_id)
                print("Task deleted successfully!")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter the task ID to mark complete: "))
                mark_task_complete(tasks, task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            save_tasks(tasks)
            print("Saving tasks to tasks.json...")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

