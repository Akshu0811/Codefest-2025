import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
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
    templates = [ { "subject": "Unusual Login Attempt Detected!", "body": "Dear User,\nWe detected an unusual login attempt on your SecureBank account from a new device.\n\nLocation: [City, Country]\nTime: [Date and Time]\n\nFor your security, we have temporarily restricted your account access. To regain access, please verify your account details within 24 hours.\n\nClick below to verify:\nVerify My Account\n\nIf you do not verify your account, it will be permanently locked.\n\nThank you for choosing SecureBank.\n\nSincerely,\nSecureBank Support Team" }, { "subject": "Your Order #12345 Has Been Placed", "body": "Hello,\n\nThank you for your purchase of Apple iPhone 14 Pro ($1,299.99).\n\nOrder Summary:\n\nProduct: Apple iPhone 14 Pro\nTotal: $1,299.99\nDelivery Address: [Your Address]\nIf you did not place this order, please cancel it immediately to avoid being charged.\n\nClick here to cancel your order:\nCancel Order\n\nThank you for shopping with Amazon.\n\nAmazon Support" },{ "subject": "Suspicious Login Attempt on Your Instagram Account", "body": "Hi [Username],\n\nWe noticed an unauthorized login attempt on your Instagram account.\n\nLocation: Unknown\nDevice: iPhone 14 Pro\n\nIf this was you, no further action is required. If this wasn’t you, please secure your account by resetting your password now:\n\nSecure My Account\n\nFailure to act within 48 hours will result in account suspension for your protection.\n\nThanks,\nInstagram Security Team" }, { "subject": "Urgent: Help Victims of [Disaster] Today", "body": "Dear Supporter,\n\nThe recent [Disaster] has left thousands homeless and in need of urgent aid. Global Helping Hands is stepping up to provide food, shelter, and medical supplies.\n\nYour donation can make a difference:\n\n$10 can feed a family for a day.\n$50 can provide shelter for a week.\n$100 can save lives through medical care.\nDonate now to join us in this critical effort:\nDonate Here\n\nThank you for your kindness and generosity.\n\nSincerely,\nThe Global Helping Hands Team" },{ "subject": "Your Email Account Will Be Deactivated!", "body": "Dear [Your Name],\n\nOur system detected that your email account storage has exceeded its limit. To avoid deactivation, you must increase your storage capacity immediately.\n\nTo continue using your email without interruption, please click the link below to upgrade:\nUpgrade My Account\n\nFailure to act within 48 hours will result in permanent email deletion.\n\nRegards,\nIT Support Team\n[Your Company Name]" } ] 

if __name__ == "__main__":
    sender_email = "codefest.cadets@gmail.com"  
    sender_password = "txmy ntcz oazy tbjl"      
    recipient_email = "exhibition123dk@gmail.com"  
    
    template= random.choice(templates)
    subject = template["subject"]
    body= template["body"]
 
    send_email(sender_email, sender_password, recipient_email, subject, body)

