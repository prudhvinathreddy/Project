import sqlite3

conn = sqlite3.connect('event_database.db')
cursor = conn.cursor()

# Drop the table if it exists (to ensure we're starting fresh)
cursor.execute('DROP TABLE IF EXISTS classes')

# Create a table to store class dates
cursor.execute('''
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT not null,
    date TEXT NOT NULL
)
''')

# Insert sample class dates (including both past and future dates)
cursor.execute('''
INSERT INTO classes (event_name,date) VALUES
('Birthday','05-01-2023'),
('Fathers Retirement','06-10-2023'),
('Reunion','07-25-2024'),
('Marriage','08-07-2024'),
('Twins Birth Day','09-12-2024'),
('Gender Reveal','12-12-2025'),
('Family union','12-12-2025')
''')

conn.commit()
conn.close()
