import unittest
from unittest.mock import patch, mock_open, MagicMock
import ziptimezone.data_manager

class TestDataManager(unittest.TestCase):
    @patch('ziptimezone.data_manager.os.makedirs')
    @patch('ziptimezone.data_manager.shutil.rmtree')
    @patch('ziptimezone.data_manager.os.path.exists')
    @patch('ziptimezone.data_manager.download_and_extract_zip_data')
    def test_refresh_data_if_needed(self, mock_download, mock_exists, mock_rmtree, mock_makedirs):
        # Set up the mock to simulate directory existence
        mock_exists.return_value = True
        
        # Run the function
        ziptimezone.data_manager.refresh_data_if_needed()
        
        # Check that rmtree was called to remove existing directory
        mock_rmtree.assert_called_once()
        # Check that makedirs was called to recreate the directory
        mock_makedirs.assert_called()
        # Check that download_and_extract_zip_data was called
        mock_download.assert_called_once()
        
        # Test the function when the directory does not exist initially
        mock_exists.return_value = False
        ziptimezone.refresh_data_if_needed()
        # Ensure rmtree is not called this time
        self.assertEqual(mock_rmtree.call_count, 1)  # still one from the first call
        # Ensure download_and_extract_zip_data is called again
        self.assertEqual(mock_download.call_count, 2)

    @patch('builtins.open', new_callable=mock_open)
    @patch('ziptimezone.data_manager.zipfile.ZipFile')
    @patch('ziptimezone.data_manager.requests.get')
    @patch('ziptimezone.data_manager.os.remove')
    def test_download_and_extract_zip_data(self, mock_remove, mock_get, mock_zip, mock_file):
        # Setup mock for requests.get
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response
        mock_response.content = b"Fake zip file content"
        
        # Configure the mock for zipfile.ZipFile
        mock_zip_instance = MagicMock()
        mock_zip.return_value.__enter__.return_value = mock_zip_instance
        
        # Run the function
        ziptimezone.data_manager.download_and_extract_zip_data('http://example.com/data.zip', '/fake/dir')
        
        # Assert file operations
        mock_file.assert_called_once_with('/fake/dir\\US.txt.zip', 'wb')
        mock_zip_instance.extractall.assert_called_once_with('/fake/dir')
        mock_remove.assert_called_once_with('/fake/dir\\US.txt.zip')
        mock_response.raise_for_status.assert_called_once()

if __name__ == '__main__':
    unittest.main()
