import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_date_diff(self):
        self.assertEquals(date_diff("1-1-2018", "1-1-2020"), 731)
        self.assertEquals(date_diff("25-12-1999", "9-3-2000"), 76)
        self.assertEquals(date_diff("25-12-1999", "9-13-2000"), -1)
        self.assertEquals(date_diff("32-12-1999", "9-12-2000"), -1)
        self.assertEquals(date_diff("32-12-1999", "29-2-2021"), -1)


