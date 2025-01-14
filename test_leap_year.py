import unittest
from leap_year import is_leap_year 

class TestLeapYear (unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(is_leap_year(1996)) # can be divided by 4 but not 100
        self.assertFalse(is_leap_year(2021)) # cannot be divided by 4
        self.assertFalse(is_leap_year(1800)) #can be divided by 100 but not by 400
        self.assertTrue(is_leap_year(2400)) #can be divided by 400
if __name__ == '__main__':
    unittest.main()