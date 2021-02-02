import unittest
from pprint import pprint
import ingester as ing

class MyTestCase(unittest.TestCase):
    def test_something(self):
        ingester = ing.Ingester()
        countries = ingester.get_countries()
        pprint(countries)

    def test_convert_currency(self):
        ingester = ing.Ingester()
        conversion = ingester.get_conversion_rate("USD", "PHP")


if __name__ == '__main__':
    unittest.main()
