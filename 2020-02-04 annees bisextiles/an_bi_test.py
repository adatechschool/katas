import unittest
from an_bi import *


class YearTest(unittest.TestCase):
    def test_bis_year_2020(self):
        lst_years = [
            2132,
            2310,
            1900,
            20,
            23,
            34500,
            0,
            -300,
        ]
        for year_iterator in range(len(lst_years)):
            yr = Year(lst_years[year_iterator])
            yr_res = yr.check_year()
            # print("{} = {}".format(lst_years[year_iterator], yr_res))
            self.assertEqual(True, yr_res)

if __name__ == '__main__':
    unittest.main()
