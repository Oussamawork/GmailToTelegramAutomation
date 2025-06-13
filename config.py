import os
from dotenv import load_dotenv

load_dotenv() 

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Split comma-separated emails into a list
ALLOWED_SENDERS = [
    sender.strip().lower()
    for sender in os.getenv("ALLOWED_SENDERS", "").split(",")
    if sender.strip()
]

if not EMAIL_ADDRESS:
    raise ValueError("EMAIL_ADDRESS environment variable is not set. Please check your .env file.")
if not EMAIL_PASSWORD:
    raise ValueError("EMAIL_PASSWORD environment variable is not set. Please check your .env file.")
if not ALLOWED_SENDERS:
    raise ValueError("ALLOWED_SENDERS environment variable is not set or empty. Please check your .env file.")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set. Please check your .env file.")
if not TELEGRAM_CHANNEL_ID:
    raise ValueError("TELEGRAM_CHANNEL_ID environment variable is not set. Please check your .env file.")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your .env file.")