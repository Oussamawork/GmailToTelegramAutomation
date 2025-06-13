import os
from dotenv import load_dotenv

load_dotenv() 

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")


# Split comma-separated emails into a list
ALLOWED_SENDERS = [
    sender.strip().lower()
    for sender in os.getenv("ALLOWED_SENDERS", "").split(",")
    if sender.strip()
]

if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, ALLOWED_SENDERS, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID]):
    raise ValueError("One or more environment variables are not set. Please check your .env file.")