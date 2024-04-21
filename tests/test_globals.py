import unittest
from unittest.mock import patch, mock_open
import ziptimezone.globals


class TestGlobals(unittest.TestCase):
    def setUp(self):
        self.mock_csv_data = (
            "country_code\tpostal_code\tplace_name\tadmin_name1\tadmin_code1\tadmin_name2\tadmin_code2\tadmin_name3\tadmin_code3\tlatitude\tlongitude\taccuracy\n"
            "US\t90210\tBeverly Hills\tCalifornia\tCA\tLos Angeles County\t06037\t-\t-\t34.0901\t-118.4065\t1\n"
            "US\t10001\tNew York City\tNew York\tNY\tNew York County\t36061\t-\t-\t40.7128\t-74.0060\t1"
        )
        self.expected_data = {
            "90210": {"latitude": "34.0901", "longitude": "-118.4065"},
            "10001": {"latitude": "40.7128", "longitude": "-74.0060"},
        }

    @patch("builtins.open", new_callable=mock_open, read_data="mock_csv_data")
    @patch("csv.DictReader")
    def test_load_zip_data_not_loaded(self, mock_dict_reader, mock_file):
        """Test load_zip_data function when there is no data loaded yet."""
        mock_dict_reader.return_value = iter(
            [
                {
                    "postal_code": "90210",
                    "latitude": "34.0901",
                    "longitude": "-118.4065",
                },
                {
                    "postal_code": "10001",
                    "latitude": "40.7128",
                    "longitude": "-74.0060",
                },
            ]
        )

        # Assume globals.loaded_zip_data is None to simulate first-time loading
        ziptimezone.globals.loaded_zip_data = None

        # Call the function
        result = ziptimezone.globals.load_zip_data("fake_path.csv")
        self.assertEqual(result, self.expected_data)

        # Verify that open was called correctly
        mock_file.assert_called_once_with("fake_path.csv", newline="", encoding="utf-8")
        # Verify that the reader was used
        mock_dict_reader.assert_called_once()

    def test_get_loaded_zip_data(self):
        """Test whether get_loaded_zip_data returns the loaded data."""
        ziptimezone.globals.loaded_zip_data = self.expected_data
        result = ziptimezone.globals.get_loaded_zip_data()
        self.assertEqual(result, self.expected_data)

    def test_load_zip_data_already_loaded(self):
        """Ensure that data isn't reloaded if it's already loaded."""
        ziptimezone.globals.loaded_zip_data = self.expected_data
        result = ziptimezone.globals.load_zip_data("fake_path.csv")
        self.assertEqual(result, self.expected_data)


if __name__ == "__main__":
    unittest.main()
