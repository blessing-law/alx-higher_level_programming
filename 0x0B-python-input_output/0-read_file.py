#!/usr/bin/python3
"""
Module that reads and prints contentes of file
to standout"""


def read_file(filename=""):
    """Function that prints to stdout"""
    with open(filename, encoding="utf-8") as a:
        a_file = a.read()
        print(a_file)
