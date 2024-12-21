import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


# function to send a notification via telegram
def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
    }
    response = requests.get(url, params=params)
