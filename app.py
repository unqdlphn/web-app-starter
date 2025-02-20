from flask import Flask, render_template # Import necessary modules
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Example: Fetch data from the database
    # ...
    conn.close()
    return render_template('index.html')  # Example: Render an HTML template

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production