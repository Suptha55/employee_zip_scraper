import requests
import logging
from config import ZIP_URL, ZIP_PATH, MAX_RETRIES, TIMEOUT

def download_zip():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logging.info(f"Attempt {attempt}: Downloading ZIP file")
            response = requests.get(ZIP_URL, timeout=TIMEOUT)
            response.raise_for_status()

            with open(ZIP_PATH, "wb") as f:
                f.write(response.content)

            logging.info("ZIP file downloaded successfully")
            return True

        except Exception as e:
            logging.error(f"Download failed: {e}")

    return False
