"""Unittest for the `Rectangle` class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Handleing of `Rectangle` class test cases"""

    def test_width_height_integers(self):
        """Test class height and width"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)

    def test_with_all_argument(self):
        """Test Class with all argument"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_private_attribute_width(self):
        """Test private width attribute"""
        self.assertFalse(hasattr(Rectangle, "__width"))

    def test_private_attribute_height(self):
        """Test private width attribute"""
        self.assertFalse(hasattr(Rectangle, "__height"))
