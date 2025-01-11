
import cgi

print("Content-Type: text/html\n")
print()

form = cgi.FieldStorage()
email = form.getvalue('email')

database = set()

def add_user(email):
    if email in database:
        print("<p>Error: Email already exists.</p>")
        return

    database.add(email)
    print("<p>User added successfully!</p>")

if email:
    add_user(email)
else:
    print("<p>Please provide an email address.</p>")
