#!/usr/bin/python3
"""This module defines a json file writig function"""
import json


def save_to_json_file(my_obj, filename):
    """write object to text file in json format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
