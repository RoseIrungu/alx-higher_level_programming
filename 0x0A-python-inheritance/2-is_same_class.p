#!/usr/bin/python3
"""defining a function to check if its the same object"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
