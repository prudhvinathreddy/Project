import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Drop the table if it exists
cursor.execute('DROP TABLE IF EXISTS classes')

# Creating a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL
)
''')
#inserting data
cursor.execute('''
INSERT INTO classes (date) VALUES
('2023-05-01'),
('2023-06-01'),
('2024-07-25'),
('2024-07-30'),
('2024-09-1'),
('2025-10-01'),
('2024-11-01')
''')

conn.commit()
conn.close()
