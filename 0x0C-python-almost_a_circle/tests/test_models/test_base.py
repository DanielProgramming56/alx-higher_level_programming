"""Unittest for the `Base` class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Handling of `Base` class test cases"""

    def test_with_no_agument(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
