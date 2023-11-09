#!/usr/bin/python3
"""Contains a class `Rectangle`"""
from models.base import Base


class Rectangle(Base):
    """
    Define a sub class `Rectangle` inherit
    from Base class
    attributes:
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            width (int): width of the ractangle
            height (int): height of rectangle
            x (int): x axis of rectangle
            y (int): y axis of the rectangle
            id (int): id of the rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
