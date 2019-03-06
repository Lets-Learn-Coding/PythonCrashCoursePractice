from city import city_name
import unittest

class city_test(unittest.TestCase):

    def test_city(self):
        formcity = city_name('chicago', 'illinois')
        self.assertEqual(formcity, 'Chicago, Illinois')

unittest.main()