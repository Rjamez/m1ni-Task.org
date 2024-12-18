import sqlite3
from config import DATABASE_PATH

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect(DATABASE_PATH)

# Create tables if they don't exist
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Create Categories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        status BOOLEAN NOT NULL DEFAULT 1
    );
    ''')

    # Create Tasks table
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

    # Create History table
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

    # Create Reminders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        reminder_date TEXT,
        FOREIGN KEY (task_id) REFERENCES tasks(id)
    );
    ''')

    conn.commit()
    conn.close()

# CRUD Functions for Tasks
def add_task(title, description, due_date, priority, category_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO tasks (title, description, due_date, priority, category_id)
    VALUES (?, ?, ?, ?, ?)
    ''', (title, description, due_date, priority, category_id))

    conn.commit()
    conn.close()

def get_all_tasks():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def update_task_status(task_id, new_status):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE tasks SET status = ? WHERE id = ?
    ''', (new_status, task_id))

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM tasks WHERE id = ?
    ''', (task_id,))

    conn.commit()
    conn.close()

# CRUD Functions for Categories
def add_category(name, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO categories (name, description)
    VALUES (?, ?)
    ''', (name, description))

    conn.commit()
    conn.close()

def get_all_categories():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()

    conn.close()
    return categories
