import datetime

# Set up the logging options
consoleLog = True
fileLog = False


def log(message):
    # Get the current date and time each time the function is called
    now = datetime.datetime.now()
    
    # Format the date and time
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")  # Including seconds for better detail

    # If the consoleLog option is enabled, print the message to the console
    if consoleLog:
        print(formatted_now, message)

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
    return now.strftime("run_%Y-%m-%d-%H-%M")


def logSpace():
    log(" ")