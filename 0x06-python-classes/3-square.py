#!/usr/bin/python3

"""Square class definition"""


class Square:
    """class name"""

    def __init__(self, size=0):
        """Initializer for the Square object.

        Args:
            size (int): The size of Square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the Square object."""
        return (self.__size * self.__size)
