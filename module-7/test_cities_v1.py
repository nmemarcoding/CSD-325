# Name: Nima Memarzadeh
# Date: 11/28/2024
# Assignment: Module 7.2

import unittest
from city_functions_v1 import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test that city_country returns the correct string."""
        formatted_city = city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
