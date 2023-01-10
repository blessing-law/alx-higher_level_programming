#!/usr/bin/python3
"""
Module that defines a text file reading function"""


def read_file(filename=""):
    """Function that prints contents of file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
