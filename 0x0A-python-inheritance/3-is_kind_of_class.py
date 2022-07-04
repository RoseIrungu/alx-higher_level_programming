#!/usr/bin/python3


"""declaring a function"""


def is_kind_of_class(obj, a_class):
    """ checking if the object is instance of a class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
