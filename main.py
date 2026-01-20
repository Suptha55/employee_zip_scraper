import logging
from downloader import download_zip
from extractor import extract_zip
from validator import validate_file_exists
from parser import parse_employee_file

# 🔹 ADD THIS
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),          # Console
        logging.FileHandler("scraper.log") # File
    ]
)

def main():
    logging.info("Starting Employee ZIP Scraper pipeline")

    if not download_zip():
        logging.error("Pipeline failed during download")
        return

    extracted_file = extract_zip()
    if not extracted_file:
        logging.error("Pipeline failed during extraction")
        return

    if not validate_file_exists(extracted_file):
        logging.error("Pipeline failed during file validation")
        return

    if not parse_employee_file(extracted_file):
        logging.error("Pipeline failed during parsing")
        return

    logging.info("Employee data pipeline completed successfully")

if __name__ == "__main__":
    main()
