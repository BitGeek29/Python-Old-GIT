import csv
from email.message import EmailMessage
import smtplib


def get_credentials(filepath):
    with open("crendentials.txt", "r") as f:
        email_address = f.readline()
        email_pass = f.readline()
    return (email_address, email_pass)

def login(email_address, email_pass, s):
    s.ehlo()
    
    s.starttls()
    s.ehlo()

    s.login(email_address, email_pass, s)
    print("login")

def send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    email_address, email_pass = get_credentials("./crendentials.txt")
    login(email_address, email_pass, s)

    subject = "Welcome to Python"
    boby = """Python is an interpreted, high-level,
    general-purpose programming language.\n 
    Created by Guido van Rossum and first relased in 1991,
    Python's desgin philosophy emphasizes code readability\n 
    with its notable use of significant whitespace"""

    message = EmailMessage()
    message['Subject'] = subject

    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(cvsfile, delimiter=" ", quotechar="|")
        for email in spamreader:
            s.send_message(email_address, email[0], message)
            print("Send To " + email[0])

    s.quit()
    print("sent")

if __name__ == "__main__":
    send_mail()
    
