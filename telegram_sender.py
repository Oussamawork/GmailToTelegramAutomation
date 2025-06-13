import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def send_text_message(subject: str, body: str, urls: list):
    text = f"<b>{subject}</b>\n\n{body}"
    if urls:
        text += "\n\n🔗 Links:\n" + "\n".join(urls)
    response = requests.post(
        f"{BASE_URL}/sendMessage",
        data={
            "chat_id": TELEGRAM_CHANNEL_ID,
            "text": text,
            "parse_mode": "HTML"
        }
    )
    response.raise_for_status()

def send_attachment(filename: str, file_data: bytes):
    files = {
        'document': (filename, file_data)
    }
    response = requests.post(
        f"{BASE_URL}/sendDocument",
        data={"chat_id": TELEGRAM_CHANNEL_ID},
        files=files
    )
    response.raise_for_status()
