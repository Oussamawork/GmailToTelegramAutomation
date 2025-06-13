import re
import base64
import quopri
from email.header import decode_header
from email.message import Message
from typing import Tuple, List

def decode_text(text, encoding):
    if not encoding:
        return text
    if encoding.lower() == 'base64':
        return base64.b64decode(text).decode('utf-8', errors='ignore')
    elif encoding.lower() == 'quoted-printable':
        return quopri.decodestring(text).decode('utf-8', errors='ignore')
    else:
        return text.decode('utf-8', errors='ignore') if isinstance(text, bytes) else text

def parse_subject(msg: Message) -> str:
    decoded_subject = ''
    subject = msg.get("Subject", "")
    for part, encoding in decode_header(subject):
        decoded_subject += decode_text(part, encoding)
    return decoded_subject.strip()

def parse_body(msg: Message) -> str:
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition", "")):
                payload = part.get_payload(decode=True)
                encoding = part.get("Content-Transfer-Encoding", None)
                return decode_text(payload, encoding)
    else:
        payload = msg.get_payload(decode=True)
        encoding = msg.get("Content-Transfer-Encoding", None)
        return decode_text(payload, encoding)
    return ""

def extract_urls(text: str) -> List[str]:
    return re.findall(r'(https?://\S+)', text)

def extract_attachments(msg: Message) -> List[Tuple[str, bytes]]:
    attachments = []
    for part in msg.walk():
        if part.get("Content-Disposition") and "attachment" in part.get("Content-Disposition"):
            filename = part.get_filename()
            file_data = part.get_payload(decode=True)
            if filename and file_data:
                attachments.append((filename, file_data))
    return attachments

def parse_email(msg: Message) -> Tuple[str, str, List[str], List[Tuple[str, bytes]]]:
    subject = parse_subject(msg)
    body = parse_body(msg)
    urls = extract_urls(body)
    attachments = extract_attachments(msg)
    return subject, body, urls, attachments
