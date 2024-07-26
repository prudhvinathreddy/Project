import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Drop the table if it exists (to ensure we're starting fresh)
cursor.execute('DROP TABLE IF EXISTS classes')

# Create a table to store class dates
cursor.execute('''
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL
)
''')

# Insert sample class dates (including both past and future dates)
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
