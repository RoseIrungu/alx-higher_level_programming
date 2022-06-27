#!/usr/bin/python3
"""creating a class called Rectangle"""


class Rectangle:
    """created a class Rectangles, assigning values"""
    def _init_(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self._height * self._width

    def perimeter(self):
        if self._height == 0 or self._width == 0:
            return 0
        return (self._height + self._width) * 2

    def _str_(self):
        if self._width == 0 or self._height == 0:
            return ''
        for z in range(self.__height - 1):
            print("#" * self.__width)
        return ("#" * self.__width)
