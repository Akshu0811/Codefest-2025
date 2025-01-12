
import sqlite3  # Import SQLite library (pre-installed in Python)

# Step 1: Connect to the database (or create one if it doesn't exist)
conn = sqlite3.connect("emails.db")  # Creates 'emails.db' file in the current directory.

# Step 2: Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 3: Create a table to store email addresses (if it doesn't already exist)
# The UNIQUE constraint prevents duplicate entries for the 'email' column.
cursor.execute('''
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY,  -- Auto-incrementing unique ID for each entry
    email TEXT UNIQUE         -- Unique constraint to prevent duplicate emails
)
''')

# Step 4: Define a function to add a new email address
def add_email(email):
    try:
        # Using parameterized queries to prevent SQL injection
        cursor.execute("INSERT INTO emails (email) VALUES (?)", (email,))
        conn.commit()  # Save the changes to the database
        print(f"{email} added successfully!")
    except sqlite3.IntegrityError:
        print(f"{email} already exists in the database!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 5: Define a function to fetch all stored emails
def fetch_emails():
    cursor.execute("SELECT * FROM emails")  # Fetch all records from the emails table
    results = cursor.fetchall()  # Fetch all rows as a list of tuples
    return results

# Step 6: Example Usage
add_email("user@example.com")   # Try adding an email
add_email("user2@example.com")  # Try adding another email
add_email("user@example.com")   # Try adding a duplicate email (will be rejected)

# Step 7: Fetch and print all stored emails
print("Stored Emails:", fetch_emails())

# Step 8: Close the database connection after operations are complete
conn.close()
