#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited class instance.

    Args:
        obj (any): Object to check.
        a_class (type): Class to check with.
    Returns:
        If an Object is inheriting from a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

