# Name: Nima Memarzadeh
# Date: 11/28/2024
# Assignment: Module 7.2

import unittest
from city_functions_v3 import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test that city_country returns the correct string."""
        formatted_city = city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Test city_country with population."""
        formatted_city = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000')
    
    def test_city_country_population_language(self):
        """Test city_country with population and language."""
        formatted_city = city_country('santiago', 'chile', 5000000, 'Spanish')
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000, Spanish')

if __name__ == '__main__':
    unittest.main()
