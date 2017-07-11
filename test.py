#!/usr/bin/python
# -*- coding: utf-8 -*-
from Funciones import Funciones
import unittest

class EjemploTest(unittest.TestCase):

    def test_Hola(self):
        f = Funciones()
        self.assertEqual("Hola",f.dime_Hola())

    def test_menor_5_True(self):
        f = Funciones()
        self.assertTrue(f.menor_5(3))

    def test_menor_5_False(self):
        f = Funciones()
        self.assertFalse(f.menor_5(7))

if __name__ == '__main__':
    unittest.main()
