import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password,recipient_email, subject, body ):
     try:
     message = MIMEMultipart
     message = ["from"]= sender_email
     message = ["To"]= recipient_email
     message = ["Subject"]= subject 
