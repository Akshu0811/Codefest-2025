import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
       
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

     
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")


if __name__ == "__main__":
    sender_email = "codefest.cadets@gmail.com"  
    sender_password = "txmy ntcz oazy tbjl"      
    recipient_email = "exhibition123dk@gmail.com"  
    subject = "Unusual Login Attempt Detected! "
    body = "Dear User , /nwe have detected an unusual login attempt on your Code Cadets Account. To confirm you must click this link.Click this link to confirm this was you in 24 hours or your account will lock permanently:https://sites.google.com/d/1KSG6E8V_3YnbImZ2Q470avj_YUzwLAYS/p/1gb85ysf4Mabon538a4CyPR7Cw8Dj9C1a/edit Sincerely, The CodeCadets Team"
send_email(sender_email, sender_password, recipient_email, subject, body)

