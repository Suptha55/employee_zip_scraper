import unittest
from unittest.mock import patch

class TestEmployeeScraper(unittest.TestCase):

    @patch("downloader.download_zip")
    def test_zip_download(self, mock_download):
        mock_download.return_value = True
        self.assertTrue(mock_download())

    @patch("extractor.extract_zip")
    def test_zip_extraction(self, mock_extract):
        mock_extract.return_value = "extracted_files/Employee Sample Data.xlsx"
        self.assertIsNotNone(mock_extract())

    @patch("parser.parse_employee_file")
    def test_excel_parsing(self, mock_parse):
        mock_parse.return_value = True
        self.assertTrue(mock_parse("dummy.xlsx"))

    @patch("parser.parse_employee_file")
    def test_missing_columns(self, mock_parse):
        mock_parse.return_value = False
        self.assertFalse(mock_parse("bad.xlsx"))


if __name__ == "__main__":
    unittest.main()
