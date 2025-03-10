import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


def send_email(receiver_email: str, subject: str, file_name: str):
    load_dotenv()
    
    port = 465  # For SSL
    sender_email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
        
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    
    with open(f"files/txt/{file_name}.txt", "r") as text_file:
        text_content = text_file.read()
    
    with open(f"files/html/{file_name}.html", "r") as html_file:
        html_content = html_file.read()
        
    # Turn the messages into objects
    part1 = MIMEText(text_content, "plain")
    part2 = MIMEText(html_content, "html")
    
    # Client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    try:    
        # Create a secure SSL context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
            
        print(f"\33[32mSuccessfully sent email to {receiver_email}\33[0m")
    
    except:
        print(f"\33[31mFailed to send email to {receiver_email}\33[0m")
    