#!/usr/bin/python3


""" New class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """class rectangle inherits base geometrty"""

    def __init__(self, width, height):
        """ private instances of class rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area fo the rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """returns a string value"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
