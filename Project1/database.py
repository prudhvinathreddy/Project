import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table to store class dates
cursor.execute('''
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL
)
''')

# Insert sample class dates
cursor.execute('''
INSERT INTO classes (date) VALUES
('2025-08-01'),
('2023-09-01'),
('2023-10-01')
''')

conn.commit()
conn.close()
