# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:15:40 2020

@author: Antonio
"""


  
import unittest
import prueba_unitaria #el nombre de tu archivo de codigo a probar


class Testprueba (unittest.TestCase):

    def test_suma(self):
        self.assertEqual(prueba_unitaria.suma(10, 5), 15)
        self.assertEqual(prueba_unitaria.suma(-1, 1), 0)
        self.assertEqual(prueba_unitaria.suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(prueba_unitaria.resta(10, 5), 5)
        self.assertEqual(prueba_unitaria.resta(-1, 1), -2)
        self.assertEqual(prueba_unitaria.resta(-1, -1), 0)

    def test_multiplicacion(self):
        self.assertEqual(prueba_unitaria.multiplicacion(10, 5), 50)
        self.assertEqual(prueba_unitaria.multiplicacion(-1, 1), -1)
        self.assertEqual(prueba_unitaria.multiplicacion(-1, -1), 1)

    def test_division(self):
        self.assertEqual(prueba_unitaria.division(10, 5), 2)
        self.assertEqual(prueba_unitaria.division(-1, 1), -1)
        self.assertEqual(prueba_unitaria.division(-1, -1), 1)
        self.assertEqual(prueba_unitaria.division(5, 2), 2.5)

    

if __name__ == '__main__':
    unittest.main()