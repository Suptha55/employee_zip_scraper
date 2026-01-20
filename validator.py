import logging
import os

def validate_file_exists(file_path):
    if not os.path.exists(file_path):
        logging.error("Extracted file does not exist")
        return False

    logging.info("Extracted file exists and is accessible")
    return True
