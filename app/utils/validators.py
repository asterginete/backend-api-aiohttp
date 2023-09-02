import re
from datetime import datetime

def validate_email(email):
    """
    Validate an email address.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_password(password):
    """
    Validate a password based on certain criteria.
    """
    # At least 8 characters, 1 uppercase, 1 lowercase, 1 number, 1 special character
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(password_regex, password))

def validate_date(date_str, format="%Y-%m-%d"):
    """
    Validate a date string based on the provided format.
    """
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

def validate_price(price):
    """
    Validate a price to ensure it's a positive number.
    """
    return price > 0

