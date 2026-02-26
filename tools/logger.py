import logging


def get_logger(name: str) -> logging.Logger:
    # Initialize a logger with the specified name
    logger = logging.getLogger(name)

    # Set the logging level to DEBUG for the logger
    # so it handles all messages from DEBUG and above
    logger.setLevel(logging.DEBUG)

    # Create a handler that will output logs to the console
    handler = logging.StreamHandler()

    # Set the logging level to DEBUG for the handler
    # so it handles all messages from DEBUG and above
    handler.setLevel(logging.DEBUG)

    # Define the log message format: include timestamp, logger name, level, and message
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)  # Apply the formatter to the handler

    # Add the handler to the logger
    logger.addHandler(handler)

    # Return the configured logger
    return logger