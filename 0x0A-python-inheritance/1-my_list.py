#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """function that sorts a list"""

    def print_sorted(self):
        """Print a sorted list."""
        print(sorted(self))
