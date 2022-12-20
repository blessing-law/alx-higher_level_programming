#!/usr/bin/python3
"""
Class sqaure: create square class
"""


class Square:
    """Define sqaure"""

    def __init__(self, size=0):
        """Initialise square class.
        Args:
            Size: size of the square.
        Raises:
            TypeError: if size is not int.
            ValueError: if size is less than zero.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else: self.__size = size
