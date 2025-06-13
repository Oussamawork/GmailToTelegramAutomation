import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ALLOWED_SENDER = os.getenv("ALLOWED_SENDER")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, ALLOWED_SENDER, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID]):
    raise ValueError("One or more environment variables are not set. Please check your .env file.")