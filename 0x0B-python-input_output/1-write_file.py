#!/usr/bin/python3


""" defining a function"""


def write_file(filename="", text=""):
    """ returns no of characters"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
