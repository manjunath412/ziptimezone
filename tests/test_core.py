import unittest
from unittest.mock import patch
from ziptimezone.core import get_timezone_by_zip
from ziptimezone.mappings import map_timezone_to_region
from ziptimezone.globals import get_loaded_zip_data


# another test
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


if __name__ == "__main__":
    unittest.main()
