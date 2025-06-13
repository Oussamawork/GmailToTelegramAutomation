import imaplib
import email
from email.message import Message
from typing import List
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, ALLOWED_SENDERS

def connect_to_gmail():
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        return imap
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Gmail: {e}")

def fetch_unread_emails_from_sender(imap) -> List[Message]:
    imap.select("inbox")
    messages = []

    for sender in ALLOWED_SENDERS:
        status, data = imap.search(None, f'(UNSEEN FROM "{sender}")')
        if status != "OK":
            continue

        for num in data[0].split():
            _, msg_data = imap.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    messages.append(msg)

    return messages

def close_connection(imap):
    imap.close()
    imap.logout()
