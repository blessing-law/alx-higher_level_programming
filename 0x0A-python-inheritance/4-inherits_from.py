#!/usr/bin/python3
"""
    Check if object is instance of inherited class
"""


def inherits_from(obj, a_class):
    """Returns true if object is instance of class
        that inherited from specified class"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
