#!/usr/bin/python3


"""new class """


class MyInt(int):

    """class int inherits items"""

    def __eq__(self, other):
        """returns false if its equal"""

        return False

    def __ne__(self, other):
        """ returns False if they are not equal"""

        return True
