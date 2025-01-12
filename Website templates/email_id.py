
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# In-memory set to store unique email IDs
email_set = set()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            if email in email_set:
                message = f"Email '{email}' already exists in memory."
            else:
                email_set.add(email)
                message = f"Email '{email}' stored successfully!"
            return render_template('login.html', message=message, emails=email_set)
    return render_template('login.html', emails=email_set)

if __name__ == '__main__':
    app.run(debug=True)