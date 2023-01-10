#!/usr/bin/python3
"""Defines a pyhton class to json"""


def class_to_json(obj):
    """Return the dicitonary representation of data structure"""
    return obj.__dict__
