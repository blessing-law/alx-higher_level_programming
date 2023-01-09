#!/usr/bin/python3

"""inherits from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define a rectangle"""

    def __init__(self, width, height):
        """initialize new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
