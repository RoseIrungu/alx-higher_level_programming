#!/usr/bin/python3


"""creating a new class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class sqaure inherits rectangle"""

    def __init__(self, size):
        """creating an instance of class rectangle"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ defining the area method"""

        return self.__size ** 2

    def __str__(self):
        """calling the string method"""

        return f"[Rectangle] {self.__size}/{self.__size}"
