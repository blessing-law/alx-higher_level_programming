#!/usr/bin/python3
"""
    Module that returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """This function returns all attributes and methods of an object"""
    return dir(obj)