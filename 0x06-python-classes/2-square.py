#!/usr/bin/python3
"""Square
create square class
"""


class Sqaure:
    """define sqaure"""

    def __init__(self, size=0):
        """initialise square class.
        Args:
            size: size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than zero
        """
        if type(size) is int:
            if size >= 0:
                self.__size__ = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
