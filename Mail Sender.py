import sys
from email.mime.text import MIMEText
import smtplib

sender_email = "oakcodecadets@gmail.com"
sender_password = "woeu sbxx reqz abby"
phistechnique  = sys.argv[1]
learners = sys.argv[2:]

def generate_phish(phishtemplate):
    with open('templates/'+phistechnique+'.txt', 'r') as file:
        subject = file.read().rstrip()
    with open('templates/'+phistechnique+'.html', 'r') as file:
        data = file.read().rstrip()
    return subject, data


def send_phish(subject, data, hacker, targets, apppassword):
    msg = MIMEText(data, 'html')
    msg['Subject'] = subject
    msg['From'] = hacker
    msg['To'] = ', '.join(targets)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(hacker, apppassword)
       smtp_server.sendmail(hacker, targets, msg.as_string())
    print("Message Succesfully sent!")


subject, data = generate_phish(phistechnique)
send_phish(subject, data, sender_email, learners, sender_password)

