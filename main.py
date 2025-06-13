from gmail_reader import connect_to_gmail, fetch_unread_emails_from_sender, close_connection
from email_parser import parse_email
from telegram_sender import send_text_message, send_attachment
from email_summarizer import summarize_text

def run():
    imap = connect_to_gmail()
    try:
        emails = fetch_unread_emails_from_sender(imap)
        if not emails:
            print("No new emails from allowed senders.")
            return

        for msg in emails:
            subject, body, urls, attachments = parse_email(msg)

            # Summarize the body text using Hugging Face API
            try:
                summarized_body = summarize_text(body)
            except Exception as e:
                print(f"Summarization failed: {e}")
                summarized_body = body[:1000] + "..." if len(body) > 1000 else body  # fallback

            send_text_message(subject, summarized_body, urls)
            for filename, file_data in attachments:
                send_attachment(filename, file_data)

    finally:
        close_connection(imap)

if __name__ == "__main__":
    run()
