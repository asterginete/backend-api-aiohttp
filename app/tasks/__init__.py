from app.services.email_service import send_email

async def send_welcome_email(user_email):
    subject = "Welcome to Our Platform!"
    body = "Thank you for registering on our platform. We're glad to have you!"
    send_email(user_email, subject, body)

async def send_password_reset_email(user_email, reset_token):
    subject = "Password Reset Request"
    body = f"Click the link below to reset your password:\nhttps://example.com/reset-password/{reset_token}"
    send_email(user_email, subject, body)
