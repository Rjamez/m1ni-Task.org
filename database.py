import sqlite3
from datetime import datetime

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('task_manager.db')
cursor = conn.cursor()

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

# Add a new task
def add_task(title, description, due_date, priority, category_id):
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority, category_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, due_date, priority, category_id))
    conn.commit()
    print("Task added successfully!")

# Other CRUD functions (e.g., update_task_status, view_tasks, etc.) can be added here as before.

# Close connection at the end
def close_connection():
    conn.close()
