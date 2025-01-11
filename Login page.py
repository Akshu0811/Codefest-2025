from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect('emails.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL
                    )''')

@app.route('/')
def index():
    return render_template('login.html')  # Ensure login.html exists in templates folder

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')

    if email and email.endswith('@gmail.com'):
        try:
            # Store the email in the database
            with sqlite3.connect('emails.db') as conn:
                conn.execute("INSERT INTO users (email) VALUES (?)", (email,))
                conn.commit()

            # Provide feedback to the user
            return render_template('result.html', message="Email successfully stored!")

        except sqlite3.IntegrityError:
            return render_template('result.html', message="This email is already registered.")
    else:
        return render_template('result.html', message="Invalid email address. Please try again.")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
