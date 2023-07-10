#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Base Geometry Class."""

    def area(self):
        """TODO: need implement."""
        raise Exception("area() will be implemented soon")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): argument's name.
            value (int): argument itself.
        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

