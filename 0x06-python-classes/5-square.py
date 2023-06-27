#!/usr/bin/python3

"""Square class definition"""


class Square:
    """class name."""

    def __init__(self, size):
        """Initializer for the Square object.

        Args:
            size (int): The size of the Square object.
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

    def my_print(self):
        """Display the Square object."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
