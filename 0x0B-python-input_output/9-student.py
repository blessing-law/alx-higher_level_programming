#!/usr/bin/python3
"""Defines a class called student"""


class Student:
    """Reprents a student"""

    def __init__(self, first_name, last_name, age):
        """Initioalize student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of othe student
            age(int): The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dictionary representaion of student"""
        return self.__dict__
