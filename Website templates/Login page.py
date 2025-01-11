import cgi
from hashlib import sha256

print("Content-Type: text/html\n")
print()

form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')

database = {}

def add_user(email, password):
    if email in database:
        print("<p>Error: Email already exists.</p>")
        return

    database[email] = sha256(password.encode()).hexdigest()
    print("<p>User added successfully!</p>")

if email and password:
    add_user(email, password)
else:
    print("<p>Please provide both email and password.</p>")

