#!/usr/bin/python3

""" function"""


def add_attribute(object, attribute, value):
    """ has attributes object and value """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
