import smtplib
from email.message import EmailMessage
from app.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(recipient, subject, body):
    """
    Send an email to the specified recipient.
    """
    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = recipient

    # Send the email using SMTP
    try:
        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {recipient} with subject '{subject}'")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")

