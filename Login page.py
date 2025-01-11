import cgi

# Get the form data
form = cgi.FieldStorage()
email = form.getvalue('email')

# Define the file path
file_path = 'emails.txt'

# Check if the email already exists in the file
email_exists = False
try:
    with open(file_path, 'r') as file:
        for line in file:
            if email.strip() == line.strip():
                email_exists = True
                break
except FileNotFoundError:
    pass  # If the file does not exist, we will create it later

# If the email does not exist, write it to the file
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

