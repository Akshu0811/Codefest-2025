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
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"Email sent successfully to {recipient_email}!")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")


if __name__ == "__main__":
    
    sender_email = "oakcodecadets@gmail.com"
    sender_password = "woeu sbxx reqz abby"  
    recipient_email="Ishanbansal2012@gmail.com"
  
    subject = input("Enter the email subject: ")


   
    template_file = "phishingEmailtemplates.txt"  
    templates = load_templates(template_file)

    if not templates:
        print("No templates available. Exiting.")
        sys.exit(1)

   
    for recipient_email in recipients:
       
        selected_template = random.choice(templates).strip()

        
        personalized_body = selected_template.format(name=recipient_email.split("@")[0])

    
        send_email(sender_email, sender_password, recipient_email, subject, personalized_body)





              




    

