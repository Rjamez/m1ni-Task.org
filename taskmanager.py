import sqlite3
from datetime import datetime

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('task_manager.db')
cursor = conn.cursor()

# Create tables if they don't already exist
def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status BOOLEAN NOT NULL DEFAULT 1
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT CHECK(priority IN ('Low', 'Medium', 'High')),
            status BOOLEAN NOT NULL DEFAULT 0,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            updated_at TEXT,
            old_status TEXT,
            new_status TEXT,
            old_priority TEXT,
            new_priority TEXT,
            FOREIGN KEY (task_id) REFERENCES tasks(id)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            reminder_date TEXT,
            FOREIGN KEY (task_id) REFERENCES tasks(id)
        );
    ''')

# Insert a new task
def add_task(title, description, due_date, priority, category_id):
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority, category_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, due_date, priority, category_id))
    conn.commit()
    print("Task added successfully!")

# View all tasks
def view_tasks():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Due: {task[3]}, Priority: {task[4]}, Status: {'Completed' if task[5] else 'Incomplete'}, Category ID: {task[6]}")
    else:
        print("No tasks available.")

# View all categories
def view_categories():
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    if categories:
        for category in categories:
            print(f"ID: {category[0]}, Name: {category[1]}, Description: {category[2]}")
    else:
        print("No categories available.")

# Add a new category
def add_category(name, description):
    cursor.execute('''
        INSERT INTO categories (name, description) 
        VALUES (?, ?)
    ''', (name, description))
    conn.commit()
    print(f"Category '{name}' added successfully!")

# Update task status
def update_task_status(task_id, new_status, new_priority):
    cursor.execute('''
        SELECT * FROM tasks WHERE id = ?
    ''', (task_id,))
    task = cursor.fetchone()

    if task:
        old_status = task[5]  # The current status
        old_priority = task[4]  # The current priority
        cursor.execute('''
            UPDATE tasks
            SET status = ?, priority = ?
            WHERE id = ?
        ''', (new_status, new_priority, task_id))

        # Log the change in history
        cursor.execute('''
            INSERT INTO history (task_id, updated_at, old_status, new_status, old_priority, new_priority)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (task_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), old_status, new_status, old_priority, new_priority))
        conn.commit()
        print(f"Task {task_id} updated successfully!")
    else:
        print(f"Task with ID {task_id} not found.")

# Add a reminder for a task
def add_reminder(task_id, reminder_date):
    cursor.execute('''
        INSERT INTO reminders (task_id, reminder_date)
        VALUES (?, ?)
    ''', (task_id, reminder_date))
    conn.commit()
    print(f"Reminder added for task {task_id}!")

# Main Menu CLI
def main_menu():
    while True:
        print("\n=== Task Manager CLI ===")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Add a Category")
        print("4. View Categories")
        print("5. Update Task Status")
        print("6. Add Reminder to Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add Task
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low, Medium, High): ")
            category_id = int(input("Enter category ID (e.g., 1 for 'Work'): "))
            add_task(title, description, due_date, priority, category_id)

        elif choice == '2':
            # View Tasks
            view_tasks()

        elif choice == '3':
            # Add Category
            name = input("Enter category name: ")
            description = input("Enter category description: ")
            add_category(name, description)

        elif choice == '4':
            # View Categories
            view_categories()

        elif choice == '5':
            # Update Task Status
            task_id = int(input("Enter task ID to update: "))
            new_status = int(input("Enter new status (0 for Incomplete, 1 for Completed): "))
            new_priority = input("Enter new priority (Low, Medium, High): ")
            update_task_status(task_id, new_status, new_priority)

        elif choice == '6':
            # Add Reminder to Task
            task_id = int(input("Enter task ID for reminder: "))
            reminder_date = input("Enter reminder date (YYYY-MM-DD HH:MM:SS): ")
            add_reminder(task_id, reminder_date)

        elif choice == '7':
            # Exit
            print("Exiting Task Manager CLI...")
            break

        else:
            print("Invalid choice. Please try again.")

# Initialize the tables
create_tables()

# Start the application
main_menu()

# Close the connection when done
conn.close()
