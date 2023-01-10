#!/usr/bin/python3
"""This module defines a json file reading function"""
import json


def load_from_json_file(filename):
    """creates python object from json file"""
    with open(filename) as f:
        return json.load(f)
