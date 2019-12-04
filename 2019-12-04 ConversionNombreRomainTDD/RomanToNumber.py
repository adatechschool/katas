import unittest
from chiffre import *

class Convert(unittest.TestCase):
    def test_I_renvoie_1(self):
        self.assertEqual(1,convertion("I"))

    def test_II_renvoie_2(self):
        self.assertEqual(2,convertion("II"))

    def test_VI_renvoie_6(self):
        self.assertEqual(6,convertion("VI"))
   
    def test_X_renvoie_10(self):
        self.assertEqual(10,convertion("X"))
    
    def test_IV_renvoie_4(self):
        self.assertEqual(4,convertion("IV"))
unittest.main()
