#!/usr/bin/python3
"""
    Defines class base geometery
"""


class BaseGeometry:
    """Class represents a base geometry"""

    def area(self):
        """method not implemeted yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as an integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
