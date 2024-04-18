import unittest
from ziptimezone.core import get_timezone_by_zip
from ziptimezone.mappings import map_timezone_to_region

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

if __name__ == '__main__':
    unittest.main()
