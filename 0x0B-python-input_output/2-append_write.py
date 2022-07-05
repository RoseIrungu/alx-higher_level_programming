#!/usr/bin/python3


"""defining a function"""


def append_write(filename="", text=""):
    """ appends a string at the end of the text file"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
