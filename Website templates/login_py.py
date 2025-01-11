
import os

def load_emails(file_name="emails.txt"):
    if os.path.exists(emails.txt):  # Check if the file exists
        try:
            with open(emails.txt, "r") as file:
                emails = file.read().splitlines()  # Read all lines and split by newline
                return emails
        except Exception as e:
            print(f"An error occurred while loading emails: {e}")
            return []
    else:
        print("File does not exist. Returning an empty list.")
        return []  # Return an empty list if no file exists

def save_emails(emails, file_name="emails.txt"):
    try:
        with open(emails.txt, "w") as file:
            for email in emails:
                file.write(email + "\n")  # Write each email on a new line
    except Exception as e:
        print(f"An error occurred while saving emails: {e}")

def add_email(new_email, emails.txt="emails.txt"):
    emails = load_emails(emails.txt)  # Load current emails
    if new_email not in emails:  # Check if the email already exists
        emails.append(new_email)  # Add the new email
        save_emails(emails, emails.txt)  # Save the updated list
        print(f"Email {new_email} added successfully!")
    else:
        print(f"Email {new_email} already exists!")  # Inform the user if email exists

def get_emails(emails.txt="emails.txt"):
    emails = load_emails(emails.txt)
    if emails:
        print("Stored Emails:")
        for email in emails:
            print(email)
    else:
        print("No emails found.")

# Example usage:
email = "user@example.com"
add_email(email)
get_emails()

