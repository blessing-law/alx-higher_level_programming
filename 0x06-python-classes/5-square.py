#!/usr/bin/python3
"""
Class sqaure: create square class
"""


class Square:
    """Define sqaure"""

    def __init__(self, size=0):
        """Initialise square class."""
        self.size = size

    @property
    def size(self):
        """Return size of square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """sets value for square object
        Args:
            Size: size of the square.
        Raises:
            TypeError: if size is not int.
            ValueError: if size is less than zero.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area of sqaure"""
        return(self.__size * self.__size)

    def my_print(self):
        """print square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
