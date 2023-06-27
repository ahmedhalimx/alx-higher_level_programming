#!/usr/bin/python3

"""Define a a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """class name."""

    def __init__(self, radius=0):
        """Initializer for the MagicClass object.

        Arg:
            radius (float or int): The radius of the MagicClass object.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass object."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass object."""
        return (2 * math.pi * self.__radius)
