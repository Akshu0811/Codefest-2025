import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password,recipient_email, subject, body ):
     try:
     message = MIMEMultipart
     message = ["from"]= sender_email
     message = ["To"]= recipient_email
     message = ["Subject"]= subject 
     message = ["Subject"]= subject

     message.attach(MIMEText(body' "plain"))
                             
     with smtlib.SMTP("smtp.gmail.com", 587) as server:
          server.starttls()
          server.login(sender_email, sender_password)
          server.sendmail.(sender_email, sender_password)

      print("Email sent sucessfully!") 

     expect Exception as e:
          print (f"failed to send email. Error: {e}")

 if __name__==__main__":
     sender_email= "oakcodecadets@gmail.com"
     sender_password= "woeu sbxx reqz abby"
     recipient_email= "recipient_email"
     subject= ""
     body= ""
send_email(sender_email, sender_password, recipient_email, subject, body)

    




              




    
