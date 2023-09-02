from app.services.email_service import send_email
import asyncio

async def send_welcome_email(user_email):
    """
    Send a welcome email to the new user.
    """
    subject = "Welcome to Our Platform!"
    body = "Thank you for registering on our platform. We're glad to have you!"
    send_email(user_email, subject, body)
    
    # Simulate some asynchronous email sending delay
    await asyncio.sleep(1)

async def send_password_reset_email(user_email, reset_token):
    """
    Send a password reset email with the provided token.
    """
    subject = "Password Reset Request"
    body = f"Click the link below to reset your password:\nhttps://example.com/reset-password/{reset_token}"
    send_email(user_email, subject, body)
    
    # Simulate some asynchronous email sending delay
    await asyncio.sleep(1)

async def send_order_confirmation_email(user_email, order_id):
    """
    Send an order confirmation email to the user.
    """
    subject = "Order Confirmation"
    body = f"Thank you for your order! Your order ID is: {order_id}. You'll receive another email when your order is shipped."
    send_email(user_email, subject, body)
    
    # Simulate some asynchronous email sending delay
    await asyncio.sleep(1)

async def send_newsletter_email(user_email, content):
    """
    Send a newsletter email to the user.
    """
    subject = "Monthly Newsletter"
    body = content
    send_email(user_email, subject, body)
    
    # Simulate some asynchronous email sending delay
    await asyncio.sleep(1)
