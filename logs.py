import logging
import sys
import os
from utils.helper import *

# Example code that might raise an exception
try:
    1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message = (
        f"[Exception Type: {exc_type.__name__}]-"
        f"[FileName: {fname}]-"
        f"[Code Line no: {exc_tb.tb_lineno}]-"
        f"[Exact Error : {str(exc_obj)}]"
    )
    print("=======================")
    print(error_message)
    django_log(error_message)

# Example log messages to demonstrate the logging format
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

