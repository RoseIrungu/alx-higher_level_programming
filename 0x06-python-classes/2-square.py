#!/usr/bin/python3
""" create a class Square with attribute size"""


class Square:
    """ Class square throws an exception message of TypeError and ValueError"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
