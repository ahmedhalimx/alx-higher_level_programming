#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class.

    Args:
        obj (any): The object.
        a_class (type): The class to check with.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

