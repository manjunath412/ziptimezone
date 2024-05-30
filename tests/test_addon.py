import unittest
from unittest.mock import patch
from datetime import datetime
from ziptimezone.addon import get_sunrise_sunset
from ziptimezone.core import get_lat_long_for_zip, get_timezone_without_map_by_zip


class TestGetSunriseSunset(unittest.TestCase):
    def setUp(self):
        self.zip_code = "90210"
        self.sample_date = datetime(2024, 7, 4).date()

    @patch("ziptimezone.core.get_lat_long_for_zip")
    @patch("ziptimezone.core.get_timezone_without_map_by_zip")
    def test_sunrise_sunset_today(self, mock_get_timezone, mock_get_lat_long):
        # Mocking the functions to return predefined values
        mock_get_lat_long.return_value = (
            34.0901,
            -118.4065,
        )  # Example coordinates for Beverly Hills
        mock_get_timezone.return_value = (
            "America/Los_Angeles"  # Timezone for Beverly Hills
        )

        # Calling the function without the date parameter, which should default to today's date
        result = get_sunrise_sunset(self.zip_code)

        # Check if the dictionary contains the expected keys
        self.assertIn("sunrise_time", result)
        self.assertIn("sunset_time", result)

    @patch("ziptimezone.core.get_lat_long_for_zip")
    @patch("ziptimezone.core.get_timezone_without_map_by_zip")
    def test_sunrise_sunset_specific_date(self, mock_get_timezone, mock_get_lat_long):
        # Setup the mocks
        mock_get_lat_long.return_value = (34.0901, -118.4065)
        mock_get_timezone.return_value = "America/Los_Angeles"

        # Calling the function with a specific date
        result = get_sunrise_sunset(self.zip_code, self.sample_date)

        # Validate the results contain correct keys and mock the expected format
        self.assertIn("sunrise_time", result)
        self.assertIn("sunset_time", result)

        # Additional checks we will revisit later on these lines..
        # self.assertEqual(result['sunrise_time'], '06:05:12')
        # self.assertEqual(result['sunset_time'], '20:07:54')


if __name__ == "__main__":
    unittest.main()
