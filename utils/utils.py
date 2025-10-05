import re


def is_password_strong(password):
    pattern = r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w]{8,}$'
    return re.search(pattern, password) is not None


def is_email_valid(email):
    pattern = r'^[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.search(pattern, email) is not None
