
import json
import os


def load_emails(sumbit_email="emails.json"):
    if os.path.exists(sumbit_email):
        with open(sumbit_email, "r") as file:
            return json.load(file)
    else:
        return []


def save_emails(emails, filename="emails.json"):
    with open(filename, "w") as file:
        json.dump(emails, file)


def add_email(new_email, filename="emails.json"):
    emails = load_emails(filename)
    if new_email not in emails:  
        emails.append(new_email)
        save_emails(emails, filename)
        print(f"Email {new_email} added successfully!")
    else:
        print(f"Email {new_email} already exists!")

# Example usage:
email = "user@example.com"  
add_email(email)
