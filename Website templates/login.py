
import re
from bs4 import BeautifulSoup

# In-memory set to store unique email IDs
email_set = set()

# Function to extract and store email IDs from an HTML file
def extract_emails_from_html(login.html):
    try:
        with open(login.html, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            # Regular expression pattern for matching email addresses
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            # Find all matches in the text
            emails = re.findall(email_pattern, text)
            for email in emails:
                store_email(email)
    except FileNotFoundError:
        print(f"File '{login.html}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to store an email ID
def store_email(email):
    if email in email_set:
        print(f"Email '{email}' already exists in memory.")
    else:
        email_set.add(email)
        print(f"Email '{email}' stored successfully!")

# Function to retrieve all stored email IDs
def retrieve_all_emails():
    if email_set:
        print("Stored email IDs:")
        for email in email_set:
            print(f"- {email}")
    else:
        print("No email IDs stored.")

# Example usage
html_file_path = 'example.html'  # Replace with your HTML file path
extract_emails_from_html(html_file_path)
retrieve_all_emails()
