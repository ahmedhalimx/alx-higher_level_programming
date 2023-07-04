#!/usr/bin/python3
"""Definition of a locked class."""

class LockedClass:
    """
    Allows the user to only instantiate the
    'first_name' attribute.
    """

    __slots__ = ["first_name"]
