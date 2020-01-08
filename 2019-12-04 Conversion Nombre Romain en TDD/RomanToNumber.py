import unittest
from chiffre import *

class Convert(unittest.TestCase):
    def test_I_renvoie_1(self):
        self.assertEqual(1,conversion("I"))

    def test_II_renvoie_2(self):
        self.assertEqual(2,conversion("II"))

    def test_VI_renvoie_6(self):
        self.assertEqual(6,conversion("VI"))
   
    def test_X_renvoie_10(self):
        self.assertEqual(10,conversion("X"))
    
    def test_IV_renvoie_4(self):
        self.assertEqual(4,conversion("IV"))

    def test_IX_renvoie_9(self):
        self.assertEqual(9,conversion("IX"))

    def test_XL_renvoie_40(self):
        self.assertEqual(40,conversion("XL"))

unittest.main()
