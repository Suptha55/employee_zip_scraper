import os
import logging
import pandas as pd

REQUIRED_COLUMNS = [
    "EEID",
    "Full Name",
    "Job Title",
    "Hire Date"
]

def parse_employee_file(file_path):
    """
    Parses and validates employee data file.
    Supports Excel (.xlsx) and CSV (.csv).
    """

    logging.info(f"Parsing employee file: {file_path}")

    if not os.path.exists(file_path):
        logging.error("Parsed file does not exist")
        return False

    try:
        # Read file
        if file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            logging.error("Unsupported file format")
            return False

        logging.info(f"Rows parsed: {len(df)}")

        # Log actual columns for transparency
        logging.info("Actual columns found in file:")
        for col in df.columns:
            logging.info(f" - {col}")

        # Validate required columns
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

        if missing:
            logging.error(f"Missing required columns: {missing}")
            return False

        logging.info("Employee data validated successfully")
        logging.info("Employee data successfully scraped")

        return True

    except Exception as e:
        logging.exception(f"Parsing failed: {e}")
        return False
