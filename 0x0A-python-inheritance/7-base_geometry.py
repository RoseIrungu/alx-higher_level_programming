#!/usr/bin/python3


"""creating an class Base geometry"""


class BaseGeometry:
    """base geaomerty has an attribute area"""

    def area(self):
        """ area raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """adding a new function that validates a value"""

        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
