import unittest
from unittest.mock import patch, mock_open
from ziptimezone.core import get_timezone_by_zip
from ziptimezone.mappings import map_timezone_to_region
from ziptimezone.data_manager import download_and_extract_zip_data, get_data_file_path

class TestTimeZoneFinder(unittest.TestCase):
    def test_get_timezone_by_zip_valid(self):
        # Test with a well-known ZIP code
        result = get_timezone_by_zip('02138')  # ZIP code for New York, NY
        self.assertEqual(result, 'Eastern')

    def test_get_timezone_by_zip_invalid(self):
        # Test with an invalid ZIP code
        with self.assertRaises(ValueError):
            get_timezone_by_zip('00000')

class TestMappings(unittest.TestCase):
    def test_map_timezone_to_region_known(self):
        # Test mapping a well-known timezone
        result = map_timezone_to_region('America/New_York')
        self.assertEqual(result, 'Eastern')

    def test_map_timezone_to_region_unknown(self):
        # Test mapping an unknown timezone
        result = map_timezone_to_region('Europe/Berlin')
        self.assertEqual(result, 'Unknown')

class TestDataManager(unittest.TestCase):

    @patch('ziptimezone.data_manager.os.path.exists')
    @patch('ziptimezone.data_manager.requests.get')
    def test_download_and_extract_zip_data(self, mock_get, mock_exists):
        # Setup
        mock_exists.return_value = False
        mock_response = mock_get.return_value
        mock_response.raise_for_status = unittest.mock.Mock()
        
        # Test successful download and extraction
        with patch('builtins.open', mock_open()):
            with patch('ziptimezone.data_manager.zipfile.ZipFile') as mock_zip:
                download_and_extract_zip_data('fake_path', 'http://example.com/data.zip')
                mock_zip.assert_called_once()
                mock_response.raise_for_status.assert_called_once()

    @patch('ziptimezone.data_manager.os.path.exists')
    def test_no_download_if_file_exists(self, mock_exists):
        # Setup
        mock_exists.return_value = True

        # Test no download when file exists
        with patch('ziptimezone.data_manager.requests.get') as mock_get:
            download_and_extract_zip_data('fake_path', 'http://example.com/data.zip')
            mock_get.assert_not_called()

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
