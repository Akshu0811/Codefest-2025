
import json
import os

def load_emails(login_py="emails.json"):
    if os.path.exists(login_py):  # Check if the file exists
        with open(login_py, "r") as file:
            return json.load(file)  # Load the email data from the file
    else:
        return []  # Return an empty list if no file exists

def save_emails(emails, login_py="emails.json"):
    with open(login_py, "w") as file:
        json.dump(emails, file)  # Save the emails list into the file

def add_email(new_email, login_py="emails.json"):
    emails = load_emails(login_py)  # Load current emails
    if new_email not in emails:  # Check if the email already exists
        emails.append(new_email)  # Add the new email
        save_emails(emails, login_py)  # Save the updated list
        print(f"Email {new_email} added successfully!")
    else:
        print(f"Email {new_email} already exists!")  # Inform the user if email exists

# Example usage:
email = "user@example.com"
add_email(email)
