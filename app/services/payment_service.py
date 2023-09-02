from app.config import PAYMENT_GATEWAY_URL, PAYMENT_API_KEY

class PaymentException(Exception):
    """Custom exception for payment-related errors."""

def process_payment(payment_info):
    """
    Process a payment using the provided payment information.
    
    Args:
    - payment_info (dict): A dictionary containing payment details like 'amount', 'credit_card_number', etc.

    Returns:
    - dict: A dictionary containing the payment status and other relevant information.
    """
    # Extract payment details
    amount = payment_info.get('amount')
    credit_card_number = payment_info.get('credit_card_number')
    expiry_date = payment_info.get('expiry_date')
    cvv = payment_info.get('cvv')

    # Mock payment processing
    # In a real-world scenario, you'd integrate with a payment gateway API here.
    # For demonstration purposes, we'll just check if the credit card number ends with an even digit.
    if int(credit_card_number[-1]) % 2 == 0:
        return {
            "status": "success",
            "transaction_id": "1234567890",
            "amount": amount
        }
    else:
        raise PaymentException("Payment failed. Please check your credit card details.")

