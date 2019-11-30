from fizzbuzz import *
import unittest

class FizzbuzzTest(unittest.TestCase):

    def test_1_renvoie_1(self):
        self.assertEqual(1, fizzbuzz(1))

    def test_2_renvoie_2(self):
        self.assertEqual(2, fizzbuzz(2)) 

    def test_3_renvoie_3(self):
        self.assertEqual("fizz", fizzbuzz(3))

    def test_5_renvoie_5(self):
        self.assertEqual("buzz", fizzbuzz(5))

    def test_6_renvoie_6(self):
        self.assertEqual("fizz", fizzbuzz(6))

    def test_10_renvoie_10(self):
        self.assertEqual("buzz", fizzbuzz(10))

    def test_15_renvoie_15(self):
        self.assertEqual("fizzbuzz", fizzbuzz(15))

    def test_30_renvoie_30(self):
        self.assertEqual("fizzbuzz", fizzbuzz(30))

    def test_50_renvoie_50(self):
        self.assertEqual("buzz", fizzbuzz(50))

unittest.main()
