#!/usr/bin/python3


"""defining a function to check if its the same object"""


def is_same_class(obj, a_class):
    """ checing if the condiotion is true"""

    if type(obj) == a_class:
        return True
    else:
        return False
