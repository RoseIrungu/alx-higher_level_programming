#!/usr/bin/python3


"""creating an class Base geometry"""


from logging import exception


class BaseGeometry:
    """base geaomerty has an attribute area"""

    def area(self):
        raise Exception("area() is not implemented")
