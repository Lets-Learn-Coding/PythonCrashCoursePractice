import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.person = Employee('testy', 'test', 1)
        self.salary = 1

    def test_give_raise_def(self):
        self.person.give_raise()
        self.assertIn('5001', str(self.person.salary))

    def test_give_raise_new(self):
        self.person.give_raise(1)
        self.assertIn('2', str(self.person.salary))


unittest.main()