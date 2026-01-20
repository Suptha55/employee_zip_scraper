import zipfile
import os
import logging
from config import ZIP_PATH, EXTRACT_DIR

def extract_zip():
    try:
        os.makedirs(EXTRACT_DIR, exist_ok=True)

        with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(EXTRACT_DIR)

        logging.info("ZIP file extracted successfully")

        for file in os.listdir(EXTRACT_DIR):
            if file.endswith(".xlsx"):
                return os.path.join(EXTRACT_DIR, file)

        raise ValueError("No Excel file found in ZIP")

    except Exception as e:
        logging.error(f"ZIP extraction failed: {e}")
        return None
