#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert binary operators == and !="""

    def __eq__(self, value):
        """Override == opeartor with != operator."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator."""
        return self.real == value

