#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """class name"""

    def __init__(self, size=0):
        """Initializer for a Square object.

        Args:
            size (int): The size of the Square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
