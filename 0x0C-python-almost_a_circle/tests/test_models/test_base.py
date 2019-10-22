#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

class Testbase(unittest.TestCase):

    def test_cases(self):
        b1 = Base()
        b2 = Base(1000)
        b3 = Base("hola")
        b4 = Base([])
        b5 = Base(())
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1000)
        self.assertEqual(b3.id, "hola")
        self.assertEqual(b4.id, [])
        self.assertEqual(b5.id, ())

if __name__ == "__main__":
    unittest.main()
