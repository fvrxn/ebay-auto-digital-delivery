import requests
from datetime import datetime
from colorama import Fore, Style, init
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

tg_chat_id = os.getenv("TELEGRAM_CHAT_ID")
tg_api_token = os.getenv("TELEGRAM_API_TOKEN")

# Initialize Colorama (important for Windows compatibility)
init(autoreset=True)

# Ensure that the base 'logs' directory exists.
def ensure_log_directory():
    if not os.path.exists("logs"):
        os.makedirs("logs")

# Get the path for the log file based on the current month and date.
def get_log_file_path():
    # Ensure that the base 'logs' directory exists.
    ensure_log_directory()

    # Generate folder name based on the current month
    current_date = datetime.now()
    month_name = current_date.strftime("%B")  # Example: January
    day = current_date.strftime("%d")         # Example: 25
    monthly_folder = os.path.join("logs", month_name)

    # Create the monthly folder if it doesn't exist
    if not os.path.exists(monthly_folder):
        os.makedirs(monthly_folder)

    # Log file named 'log-25.txt' inside the monthly folder
    log_file = os.path.join(monthly_folder, f"log-{day}.txt")
    return log_file

def output(message: str, level: str = "INFO", log_to_file: bool = True, log_to_telegram: bool = False, log_to_console: bool = True):
    """
    Flexible logging function with options for file logging, console output, and Telegram integration.

    Args:
        message (str): The log message to display or save.
        level (str): Log level (e.g., INFO, WARNING, ERROR).
        log_to_file (bool): Whether to write the log message to a file.
        log_to_telegram (bool): Whether to send the log message to a Telegram chat.
        log_to_console (bool): Whether to print the log message to the console.
    """
    # Define prefixes and colors for different log levels
    levels = {
        "INFO": (Fore.GREEN, "[INFO]"),
        "WARNING": (Fore.YELLOW, "[WARNING]"),
        "ERROR": (Fore.RED, "[ERROR]"),
    }
    color, prefix = levels.get(level.upper(), (Fore.WHITE, "[LOG]"))  # Default to white "[LOG]" if level is unknown

    # Format the message with timestamp and prefix
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"{timestamp} {prefix} {message}"

    # Print the message to the console with color
    if log_to_console:
        print(color + formatted_message + Style.RESET_ALL)

    # Write the log message to a file
    if log_to_file:
        log_file = get_log_file_path()  # Get the dynamic log file path
        try:
            with open(log_file, "a") as file:
                file.write(formatted_message + "\n")
        except Exception as e:
            if log_to_console:  # Show file errors only in console if enabled
                print(f"{Fore.RED}Error writing to log file: {str(e)}{Style.RESET_ALL}")

    # Send the log message to Telegram
    if log_to_telegram:
        try:
            url = f"https://api.telegram.org/bot{tg_api_token}/sendMessage"
            payload = {
                "chat_id": tg_chat_id,
                "text": formatted_message
            }
            response = requests.post(url, data=payload)
            if response.status_code != 200 and log_to_console:
                print(f"{Fore.RED}Telegram error: {response.text}{Style.RESET_ALL}")
        except Exception as e:
            if log_to_console:  # Show Telegram errors only in console if enabled
                print(f"{Fore.RED}Error sending to Telegram: {str(e)}{Style.RESET_ALL}")