#!/usr/bin/python3

"""Square class definition."""


class Square:
    """class name"""

    def __init__(self, size=0):
        """Initializer for the Square object.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Sets the size of the Square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the Square object."""
        return (self.__size * self.__size)
