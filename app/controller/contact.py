import os
from typing import Optional

import requests
from email_validator import validate_email, EmailNotValidError


def check_email(email: str) -> (bool, Optional[str], Optional[str]):
    try:
        valid = validate_email(email)
        return True, None, valid.email
    except EmailNotValidError as e:
        return False, str(e), email


def check_message(message: str) -> (bool, Optional[str], Optional[str]):
    if len(message) == 0:
        return False, "Please enter a message.", message
    if len(message) > 2000:
        return False, "Your message must not be longer than 2000 characters.", message
    return True, None, message


def send_contact_message(email: str, message: str):
    token = os.environ.get("TELEGRAM_BOT_API_TOKEN")
    chat_id = os.environ.get("TELEGRAM_BOT_API_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": f"email: {email}\r\nmessage:{message}"
    }
    requests.post(url=url, data=data)
