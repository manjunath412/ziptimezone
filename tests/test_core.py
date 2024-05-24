import unittest
from unittest.mock import patch
from ziptimezone.core import get_timezone_by_zip, calculate_time_difference
from ziptimezone.mappings import map_timezone_to_region
from ziptimezone.globals import get_loaded_zip_data
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from pytz import timezone


class TestTimeZoneFinder(unittest.TestCase):
    @patch("ziptimezone.core.get_loaded_zip_data")
    @patch("ziptimezone.core.map_timezone_to_region")
    @patch("ziptimezone.core.TimezoneFinder")
    def test_get_timezone_by_zip_valid(self, mock_tf, mock_map, mock_get_data):
        # Set up mocks
        mock_tf_instance = mock_tf.return_value
        mock_tf_instance.timezone_at.return_value = "America/New_York"
        mock_map.return_value = "Eastern"
        mock_get_data.return_value = {
            "02138": {"latitude": "42.3770", "longitude": "-71.1256"}
        }

        # Test valid ZIP code
        result = get_timezone_by_zip("02138")
        self.assertEqual(result, "Eastern")
        mock_map.assert_called_with("America/New_York")
        mock_tf_instance.timezone_at.assert_called_with(lat=42.3770, lng=-71.1256)

    @patch("ziptimezone.core.get_loaded_zip_data")
    def test_get_timezone_by_zip_invalid(self, mock_get_data):
        # Set up mock to return None for invalid ZIP code
        mock_get_data.return_value = {}

        # Test with an invalid ZIP code
        result = get_timezone_by_zip("00000")
        self.assertEqual(
            result, "No valid geographic coordinates found for ZIP code 00000."
        )


class TestMappings(unittest.TestCase):
    def test_map_timezone_to_region_known(self):
        # Test mapping a well-known timezone
        result = map_timezone_to_region("America/New_York")
        self.assertEqual(result, "Eastern")

    def test_map_timezone_to_region_unknown(self):
        # Test mapping an unknown timezone
        result = map_timezone_to_region("Europe/Berlin")
        self.assertEqual(result, "Unknown")


"""
class TestTimeDifferenceCalculator(unittest.TestCase):

    @patch("ziptimezone.core.get_timezone_without_map_by_zip")
    @patch("ziptimezone.core.datetime")
    @patch("ziptimezone.core.timezone")
    def test_time_difference_valid(self, mock_timezone, mock_datetime, mock_get_timezone):
        # Mocking datetime and timezone behavior
        mock_get_timezone.side_effect = ["America/New_York", "America/Los_Angeles"]
        mock_timezone.side_effect = lambda x: timezone(x)
        mock_datetime.now.return_value = datetime(2022, 1, 1, 12)  # Fixed time for consistent testing
        utc = timezone('UTC')
        mock_datetime.now.return_value = utc.localize(mock_datetime.now.return_value)

        # Test with valid US ZIP codes
        result = calculate_time_difference("10001", "94102")
        self.assertIn("ahead of", result)

    @patch("ziptimezone.core.get_timezone_without_map_by_zip")
    def test_time_difference_invalid_zip(self, mock_get_timezone):
        # Set up mocks to return 'Unknown' for non-US ZIP codes
        mock_get_timezone.side_effect = ["Unknown", "America/New_York"]

        # Test with one invalid ZIP code
        result = calculate_time_difference("00000", "10001")
        self.assertEqual(result, "One or both zip codes are invalid or non-US.")

    @patch("ziptimezone.core.get_timezone_without_map_by_zip")
    def test_time_difference_exception_handling(self, mock_get_timezone):
        # Set up mocks to simulate an exception
        mock_get_timezone.side_effect = Exception("Unexpected Error")

        # Test error handling
        result = calculate_time_difference("99999", "88888")
        self.assertEqual(result, "Unexpected Error")
"""
if __name__ == "__main__":
    unittest.main()
