import sys
from src.logger import logging
def error_message_details(error,error_details: sys):
    _, _, exc_tb= error_details.exc_info()
    exc_file= exc_tb.tb_frame.f_code.co_filename
    exec_line= exc_tb.tb_lineno
    error= str(error)
    message= f"Error occur in python script at file {exc_file}, line no {exec_line}, {error}"
    return message

class Custom_Exception(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details= error_details)
    def str(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
        # logging.info("This will not be logged because of the error")  # Would not be reached
    except Exception as e:
        logging.info(f"An error occurred")  # Log the actual error
        raise Custom_Exception(e, sys)

