import datetime
from utils.telegramAPI import send_telegram_notification

# Set up the logging options
consoleLog = True
fileLog = True
telegramLog = True


def log(message, priority):
    # Get the current date and time each time the function is called
    now = datetime.datetime.now()
    
    # Format the date and time
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")  # Including seconds for better detail

    # If the consoleLog option is enabled, print the message to the console
    if consoleLog:
        print(formatted_now, message)

    # If the telegramLog option is enabled, send the message via Telegram
    if telegramLog:
        # If priority is high, send the message via Telegram
        if priority == 1:
            send_telegram_notification(message)


    # If the fileLog option is enabled, write the message to a log file
    if fileLog:
        try:
            # Open the log file in append mode
            log_file_name = logname()
            with open(f"./logs/{log_file_name}.log", "a+") as file:
                file.write(f"{formatted_now} {message}\n")
        except Exception as e:
            if consoleLog:
                print(f"Unable to write to log file: {e}")


def logname():
    # Return the current timestamp as the log file name
    now = datetime.datetime.now()
    return now.strftime("run_%Y-%m-%d")


def logSpace():
    log(" ")