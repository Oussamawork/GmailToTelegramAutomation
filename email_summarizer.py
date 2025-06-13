import os
import logging
from openai import OpenAI
from config import OPENAI_API_KEY

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text: str) -> str:
    if not OPENAI_API_KEY:
        logging.error("OpenAI API key is missing.")
        return ""

    logging.info("Starting summarization with GPT-4o")

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a smart assistant that extracts only the main informative content from a newsletter email. "
                        "Please remove ads, disclaimers, affiliate notices, unsubscribe links, and anything repetitive. "
                        "Return the cleaned-up version in readable, concise plain text. "
                        "Highlight the key takeaways, separate by sections (e.g., STOCKS, REAL ESTATE, CRYPTO)."
                        "Remove any promotional or legal filler."
                    )
                },
                {"role": "user", "content": text}
            ],
            temperature=0.5,
            max_tokens=500
        )
        result = response.choices[0].message.content.strip()
        logging.info("Summarization completed.")
        return result

    except Exception as e:
        logging.exception("Summarization failed.")
        return f"Summarization failed: {e}"