import cgi

form = cgi.FieldStorage()
email = form.getvalue('email')

file_path = 'emails.txt'

email_exists = False
try:
    with open(file_path, 'r') as file:
        for line in file:
            if email.strip() == line.strip():
                email_exists = True
                break
except FileNotFoundError:
    pass  


if not email_exists:
    with open(file_path, 'a') as file:
        file.write(email + '\n')
    print("Content-type: text/html\n")
    print("<h1>Success!</h1>")
    print("<p>Email address stored successfully.</p>")
else:
    print("Content-type: text/html\n")
    print("<h1>Error</h1>")
    print("<p>Email address already exists.</p>")

