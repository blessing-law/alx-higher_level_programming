#!/usr/bin/python3
"""this module defines a json to object funciton"""
import json


def from_json_string(my_str):
    """Returns object representation of a json string"""
    return json.loads(my_str)
