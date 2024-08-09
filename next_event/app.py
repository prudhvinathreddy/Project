from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Function to get the next event from the database
def get_next_event():
    conn = sqlite3.connect('event_database.db')
    cursor = conn.cursor()
    today = datetime.today().strftime('%m-%d-%Y')
    cursor.execute("SELECT event_name, date FROM classes WHERE date >= ? ORDER BY date ASC LIMIT 1", (today,))
    next_event = cursor.fetchone()
    conn.close()
    return next_event

@app.route('/')
def index():
    next_event = get_next_event()
    return render_template('index.html', next_event=next_event)

if __name__ == '__main__':
    app.run(debug=True)
