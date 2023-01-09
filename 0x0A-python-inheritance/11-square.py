#!/usr/bin/python3
"""defines rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size):
        """initiolize new sqaure"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size= size
