#!/usr/bin/python3


""" defining a function"""


def inherits_from(obj, a_class):
    """The fuction returns true if object is inherited"""

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
