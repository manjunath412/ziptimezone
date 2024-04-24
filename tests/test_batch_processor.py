import unittest
from unittest.mock import patch, MagicMock
from ziptimezone.core import get_timezone_by_zip, get_lat_long_for_zip
from ziptimezone.batch_processor import (
    get_timezone_for_many_zips,
    process_zip_code,
    get_lat_long_for_many_zips,
)


class TestBatchProcessor(unittest.TestCase):

    @patch("ziptimezone.batch_processor.get_timezone_by_zip")
    def test_get_timezone_for_many_zips_success(self, mock_get_timezone):
        # Setup the mock to return a timezone when called
        mock_get_timezone.return_value = "America/New_York"

        # Call the function with a list of ZIP codes
        zip_codes = ["10001", "90210", "94105"]
        expected_results = {zip_code: "America/New_York" for zip_code in zip_codes}
        results = get_timezone_for_many_zips(zip_codes)

        # Check if the results match the expected results
        self.assertEqual(results, expected_results)
        mock_get_timezone.assert_has_calls(
            [unittest.mock.call(zip_code) for zip_code in zip_codes], any_order=True
        )

    @patch("ziptimezone.batch_processor.get_timezone_by_zip")
    def test_get_timezone_for_many_zips_error(self, mock_get_timezone):
        # Setup the mock to raise an exception when called
        mock_get_timezone.side_effect = Exception("Some error")

        # Call the function with a list of ZIP codes
        zip_codes = ["10001", "90210", "94105"]
        expected_results = {zip_code: None for zip_code in zip_codes}
        results = get_timezone_for_many_zips(zip_codes)

        # Check if the results match the expected results
        self.assertEqual(results, expected_results)
        mock_get_timezone.assert_has_calls(
            [unittest.mock.call(zip_code) for zip_code in zip_codes], any_order=True
        )

    @patch("ziptimezone.batch_processor.get_lat_long_for_zip")
    def test_get_lat_long_for_many_zips_success(self, mock_get_lat_long):
        # Setup the mock to return lat and long when called
        mock_lat_long_values = {
            "10001": (40.7484, -73.9967),
            "90210": (34.0901, -118.4065),
            "94105": (37.7864, -122.3892),
        }
        mock_get_lat_long.side_effect = lambda zip_code: mock_lat_long_values.get(
            zip_code, (None, None)
        )

        # Call the function with a list of ZIP codes
        zip_codes = ["10001", "90210", "94105"]
        expected_results = mock_lat_long_values
        results = get_lat_long_for_many_zips(zip_codes)

        # Check if the results match the expected results
        self.assertEqual(results, expected_results)
        # Ensure each ZIP code was passed to the mock function
        for zip_code in zip_codes:
            mock_get_lat_long.assert_any_call(zip_code)

    @patch("ziptimezone.batch_processor.get_lat_long_for_zip")
    def test_get_lat_long_for_many_zips_error(self, mock_get_lat_long):
        # Setup the mock to raise an exception when called
        mock_get_lat_long.side_effect = Exception("Some error")

        # Call the function with a list of ZIP codes
        zip_codes = ["10001", "90210", "94105"]
        expected_results = {zip_code: (None, None) for zip_code in zip_codes}
        results = get_lat_long_for_many_zips(zip_codes)

        # Check if the results match the expected results
        self.assertEqual(results, expected_results)
        # Ensure each ZIP code was passed to the mock function
        for zip_code in zip_codes:
            mock_get_lat_long.assert_any_call(zip_code)


if __name__ == "__main__":
    unittest.main()
