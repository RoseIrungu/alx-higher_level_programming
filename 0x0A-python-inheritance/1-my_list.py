#!/usr/bin/python3
"""creating a class which inherits attributes"""


class MyList(list):
    """ class that has a list"""

    def print_sorted(self):
        print(sorted(self))
