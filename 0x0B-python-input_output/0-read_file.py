#!/usr/bin/python3


""" defining a function"""


def read_file(filename=""):
    """ it reads the text file,prints in stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
