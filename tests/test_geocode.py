import unittest
from ziptimezone.geocode import get_lat_long_for_zip

class TestGeocode(unittest.TestCase):
    def test_get_lat_long_valid(self):
        """ Test that valid ZIP codes return the correct latitude and longitude. """
        # Using the ZIP code for Beverly Hills, California
        latitude, longitude = get_lat_long_for_zip('02138')
        # Typical latitude and longitude for Beverly Hills, rounded to 4 decimal places
        self.assertAlmostEqual(latitude, 34.0901, places=4)
        self.assertAlmostEqual(longitude, -118.4065, places=4)

    def test_get_lat_long_invalid(self):
        """ Test that invalid ZIP codes return None, None. """
        # Using an obviously invalid ZIP code
        latitude, longitude = get_lat_long_for_zip('99999')
        self.assertIsNone(latitude)
        self.assertIsNone(longitude)

    def test_get_lat_long_empty(self):
        """ Test behavior with empty ZIP code input. """
        # Testing empty string
        latitude, longitude = get_lat_long_for_zip('')
        self.assertIsNone(latitude)
        self.assertIsNone(longitude)
        
        # Testing None input, if applicable based on function support
        latitude, longitude = get_lat_long_for_zip(None)
        self.assertIsNone(latitude)
        self.assertIsNone(longitude)

if __name__ == '__main__':
    unittest.main()
