pip install flask

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


def init_db():
    with sqlite3.connect('emails.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL
                    )''')


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')

    if email and email.endswith('@gmail.com'):
        try:
            with sqlite3.connect('emails.db') as conn:
                conn.execute("INSERT INTO users (email) VALUES (?)", (email,))
                conn.commit()
            return "Email successfully stored!"
        except sqlite3.IntegrityError:
            return "This email is already registered."
    else:
        return "Invalid email address. Please try again."

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

python app.py



