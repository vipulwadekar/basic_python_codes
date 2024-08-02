import os,sys
import logging
def setup_logger():
    # Define the directory and log file path
    log_directory = os.path.join(os.getcwd(), 'logs')
    log_file_path = os.path.join(log_directory, 'backend_log.log')

    # Ensure the log directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

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

# Call the setup function to configure the logger
setup_logger()




# Get the configured logger
logger = logging.getLogger('DJANGO-BACKEND')

# Functions for specific log levels
def django_log_debug(message):
    logger.debug(message)

def django_log_info(message):
    logger.info(message)

def django_log_warning(message):
    logger.warning(message)

def django_log_error(message):
    logger.error(message)

def django_log_critical(message):
    logger.critical(message)
