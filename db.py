import sqlite3

# Connect to a new SQLite database file
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create a table for tasks
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
''')

# Save and close
conn.commit()
conn.close()
