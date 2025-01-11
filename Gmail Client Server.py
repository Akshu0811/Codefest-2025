import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import random

def load_templates(template_file):
    try:
        with open(template_file, "r") as file:
            content = file.read()
        return content.split("---")  # Split templates by delimiter
    except Exception as e:
        print(f"Error loading templates: {e}")
        return []


def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))  # Use "html" for HTML content

        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"Email sent successfully to {recipient_email}!")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")


def add_redirect(template, redirect_url):
    """
    Add a redirect link to the email template.
    """
    return template.replace("{redirect_url}", redirect_url)


if __name__ == "__main__":
    # Sender email and credentials
    sender_email = "oakcodecadets@gmail.com"
    sender_password = "woeu sbxx reqz abby"
    recipient_email="akshayasivaguru08@oakridge.in"
    # Subject of the email
    subject = "Phishing Simulation Test"

    # Load templates
    template_file = "phishingEmailtemplates.html"  # Ensure this file exists
    templates = load_templates(template_file)

    if not templates:
        print("No templates available. Exiting.")
        sys.exit(1)

    # Redirect URL to be injected
    redirect_url = "https://sites.google.com/d/1KSG6E8V_3YnbImZ2Q470avj_YUzwLAYS/p/1gb85ysf4Mabon538a4CyPR7Cw8Dj9C1a/edit"

    # Send email to each recipient
    for recipient_email:
        # Select a random template
        selected_template = random.choice(templates).strip()

        # Add redirect URL
        selected_template_with_redirect = add_redirect(selected_template, redirect_url)

        # Customize the template
        personalized_body = selected_template_with_redirect.format(name=recipient_email.split("@")[0])

        # Send the email
        send_email(sender_email, sender_password, recipient_email, subject, personalized_body)
