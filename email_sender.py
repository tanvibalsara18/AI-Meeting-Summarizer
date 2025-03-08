import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def send_email(summary, recipient_email):
    subject = "Meeting Summary"
    body = f"Here’s your summarized meeting:\n\n{summary}"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, recipient_email, message)
    
    print("✅ Email sent successfully!")

if __name__ == "__main__":
    send_email("Sample Summary", "recipient@email.com")
