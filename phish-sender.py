import smtplib
from email.mime.text import MIMEText
import sys

hacker = "oakcodecadets@gmail.com"
apppassword = "woeu sbxx reqz abby"
phishtemplate = sys.argv[1]
targets = sys.argv[2:]

def generate_phish(phishtemplate):
    with open('templates/'+phishtemplate+'.txt', 'r') as file:
        subject = file.read()
    with open('templates/'+phishtemplate+'.html', 'r') as file:
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
    print("Message sent!")

subject, data = generate_phish(phishtemplate)
send_phish(subject, data, hacker, targets, apppassword)


