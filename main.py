# Import the necessary libraries
from email.mime.text import MIMEText
import random
import smtplib

# List of example spam emails
emails = [
    {
        "subject": "Special Offer",
        "body": "Half-price discount on all products!"
    },
    {
        "subject": "Monthly News",
        "body": "Here are the latest news for the month of October."
    },
    {
        "subject": "Event Invitation",
        "body": "We invite you to our annual event next month."
    }
]

# Function to get a random spam email
def get_random_email(emails_list):
    return random.choice(emails_list)

# Function to send an email
def send_email(subject, body, to_email):
    # Configuration
    sender_email = "notputtingmyemailhere@gmail.com"
    sender_password = "notmypasswordeither"

    # Create the message
    msg = MIMEText(body, "plain")
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Connect to the SMTP server
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, [to_email], msg.as_string())
    server.quit()

# Get a random email and send it
random_email = get_random_email(emails)
send_email(random_email["subject"], random_email["body"], "randomemail@gmail.com")
