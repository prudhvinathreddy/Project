from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Function to get the next class date from the database
def get_next_class_date():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("SELECT date FROM classes WHERE date >= ? ORDER BY date ASC LIMIT 1", (today,))
    next_class = cursor.fetchone()
    conn.close()
    return next_class[0] if next_class else None

@app.route('/')
def index():
    next_class_date = get_next_class_date()
    return render_template('index.html', next_class_date=next_class_date)

if __name__ == '__main__':
    app.run(debug=True)
