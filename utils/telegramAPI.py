import os
import requests


# function to send a notification via telegram
def send_telegram_notification(api_token, chat_id, message):
    url = f"https://api.telegram.org/bot{api_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    response = requests.get(url, params=params)
