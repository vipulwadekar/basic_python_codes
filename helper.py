import uuid
import os,sys
import logging


def generate_6_char_code():
    # Generate a UUID
    unique_id = uuid.uuid4()
    
    # Convert UUID to a string and remove hyphens
    unique_str = str(unique_id).replace("-", "")[8:14]
    print(f"====================>{unique_str}")

    
    # Form a 6-character code from the first 4 characters
    code = unique_str
    
    return code


def django_log(error_message):
    # Define the directory and log file path
    log_directory = os.path.join(os.getcwd(), 'logs')
    log_file_path = os.path.join(log_directory, 'backend_log.log')

    # Ensure the log directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    print(log_file_path)


    # Create a logger object
    logger = logging.getLogger('DJANGO-BACKEND')
    logger.setLevel(logging.DEBUG)  # Set the minimum logging level for the logger

    # Create a file handler

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)  # Set the minimum logging level for the file handler

    # Create a formatter with an enhanced format
    formatter = logging.Formatter(
        '[%(levelname)s] - [%(name)s] - %(asctime)s - %(message)s'
    )

    # Apply the formatter to the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)
    logger.error(error_message)