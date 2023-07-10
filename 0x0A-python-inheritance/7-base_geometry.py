#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent Base Geometry Class."""

    def area(self):
        """TODO: implement this."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an argument as an integer.

        Args:
            name (str): argument's name.
            value (int): argument vlaue.
        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
